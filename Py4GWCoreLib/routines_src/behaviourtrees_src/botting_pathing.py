"""
Reusable Botting pathing state helpers.

These helpers operate on Botting-style runtime objects, plain parameters, and
callables supplied by adapter layers.
"""
from __future__ import annotations

from time import monotonic
from typing import Callable, Iterable

from Py4GWCoreLib.routines_src.behaviourtrees_src.botting_movement import cutscene_active


LogFn = Callable[[str], None]
EnemyResolver = Callable[[], int | None]


def _noop_log(_message: str) -> None:
    return


def select_nearest_alive_enemy(
    enemy_ids,
    *,
    player_xy: tuple[float, float],
    max_distance: float,
    is_alive: Callable[[int], bool],
    get_xy: Callable[[int], tuple[float, float]],
    distance: Callable[[tuple[float, float], tuple[float, float]], float],
) -> int | None:
    nearest_id: int | None = None
    nearest_dist = float("inf")
    for raw_enemy_id in enemy_ids or []:
        enemy_id = int(raw_enemy_id)
        if not is_alive(enemy_id):
            continue
        enemy_xy = get_xy(enemy_id)
        dist = float(distance(player_xy, enemy_xy))
        if dist > float(max_distance):
            continue
        if dist < nearest_dist:
            nearest_id = enemy_id
            nearest_dist = dist
    return nearest_id


def add_pre_movement_loot_wait_state(
    bot,
    *,
    step_name: str,
    enabled: bool = True,
    timeout_ms: int = 30_000,
    poll_ms: int = 300,
    loot_range: float = 1_250.0,
    loot_wait_required: Callable[..., bool] | None = None,
) -> None:
    if not enabled or loot_wait_required is None:
        return

    def _wait_for_party_loot():
        from Py4GWCoreLib import Routines

        if timeout_ms <= 0:
            return

        deadline = monotonic() + (max(0, int(timeout_ms)) / 1000.0)
        while monotonic() < deadline and loot_wait_required(search_range=float(loot_range), bot=bot):
            if cutscene_active():
                return
            yield from Routines.Yield.wait(max(50, int(poll_ms)))

    bot.States.AddCustomState(_wait_for_party_loot, f"{step_name}: Wait Party Loot")


def add_path_to_target_state(
    bot,
    *,
    target_resolver: Callable[[], int | None],
    max_dist: float,
    tolerance: float = 150.0,
    required: bool = True,
    name: str = "Path To Target",
) -> bool:
    from Py4GWCoreLib import Agent, Player, Range, Utils

    max_distance = float(max_dist if max_dist > 0 else Range.Compass.value)
    arrival_tolerance = float(tolerance if tolerance > 0 else 150.0)

    def _enqueue_path_to_target():
        px, py = Player.GetXY()
        target_agent_id = target_resolver()
        if target_agent_id is None:
            return

        tx, ty = Agent.GetXY(target_agent_id)
        distance = Utils.Distance((px, py), (tx, ty))

        def _target_invalid(agent_id: int = target_agent_id) -> bool:
            if not Agent.IsValid(agent_id):
                return True
            if not Agent.IsAlive(agent_id):
                return True
            cx, cy = Agent.GetXY(agent_id)
            return Utils.Distance(Player.GetXY(), (cx, cy)) <= arrival_tolerance

        Player.ChangeTarget(target_agent_id)
        yield from bot.Move._coro_xy(tx, ty, name, forced_timeout=max(3000, int(distance * 4)))
        if cutscene_active():
            return
        yield from bot.Wait._coro_until_condition(_target_invalid, duration=100)

    if required or target_resolver() is not None:
        bot.States.AddCustomState(_enqueue_path_to_target, str(name))
        return True
    return False


def add_auto_path_state(
    bot,
    *,
    points: Iterable[tuple[float, float]],
    name: str,
    pause_on_combat: bool,
    pause_on_danger_was_active: bool,
    arrival_tolerance: float,
    retry_delay_ms: int,
    allow_map_transition: bool,
    max_retries: int,
    debug_log: LogFn | None = None,
    log: LogFn | None = None,
) -> None:
    from Py4GWCoreLib import Agent, GLOBAL_CACHE, Map, Player, Routines, Utils

    path_points = [(float(x), float(y)) for x, y in points]
    debug_log_fn = debug_log or _noop_log
    log_fn = log or _noop_log

    def _is_player_dead() -> bool:
        try:
            player_id = int(Player.GetAgentID() or 0)
            return bool(player_id and Agent.IsDead(player_id))
        except Exception:
            return False

    def _recovery_blocking() -> bool:
        try:
            return bool(_is_player_dead() or Routines.Checks.Party.IsPartyWiped() or GLOBAL_CACHE.Party.IsPartyDefeated())
        except Exception:
            return _is_player_dead()

    def _distance_to_target(target_x: float, target_y: float) -> float:
        try:
            px, py = Player.GetXY()
            return float(Utils.Distance((float(px), float(py)), (float(target_x), float(target_y))))
        except Exception:
            return float("inf")

    def _map_signature() -> tuple[int, int, int, int]:
        try:
            region = Map.GetRegion()
            language = Map.GetLanguage()
            return (
                int(Map.GetMapID() or 0),
                int(region[0] if isinstance(region, tuple) and region else 0),
                int(Map.GetDistrict() or 0),
                int(language[0] if isinstance(language, tuple) and language else 0),
            )
        except Exception:
            return (0, 0, 0, 0)

    map_signature_at_start = _map_signature()

    def _map_transition_detected() -> bool:
        try:
            if cutscene_active() or not Routines.Checks.Map.MapValid() or Map.IsMapLoading():
                return True
        except Exception:
            return True
        return _map_signature() != map_signature_at_start

    def _run_auto_path():
        map_transition_logged = False
        for point_i, (target_x, target_y) in enumerate(path_points):
            if cutscene_active():
                return
            attempts = 0
            while True:
                if cutscene_active():
                    return
                recovery_waited = False
                while _recovery_blocking():
                    if cutscene_active():
                        return
                    recovery_waited = True
                    yield from bot.Wait._coro_for_time(max(50, int(retry_delay_ms)))
                if recovery_waited and attempts > 0:
                    debug_log_fn(
                        f"{name}: recovery detected, resetting retries for waypoint {point_i + 1}/{len(path_points)}."
                    )
                    attempts = 0

                attempts += 1
                point_step_name = f"{name} [{point_i + 1}/{len(path_points)}]"
                movement_ok = yield from bot.Move._coro_xy(
                    target_x,
                    target_y,
                    step_name=point_step_name,
                    fail_on_unmanaged=False,
                )
                if cutscene_active():
                    return

                if not movement_ok and _map_transition_detected():
                    return

                if _map_transition_detected():
                    if allow_map_transition or cutscene_active():
                        return
                    if not map_transition_logged:
                        log_fn(
                            f"{name}: map transition detected during auto_path; "
                            "holding step until recovery/map restore to avoid stale path advance."
                        )
                        map_transition_logged = True
                    while _map_transition_detected():
                        if cutscene_active():
                            return
                        yield from bot.Wait._coro_for_time(max(50, int(retry_delay_ms)))
                    attempts = 0
                    continue

                distance = _distance_to_target(target_x, target_y)
                if distance <= float(arrival_tolerance):
                    break

                if max_retries > 0 and attempts > max_retries:
                    log_fn(
                        f"{name}: waypoint {point_i + 1}/{len(path_points)} not reached after {attempts} attempts "
                        f"(dist={distance:.0f}, tol={float(arrival_tolerance):.0f}); resetting retry cycle."
                    )
                    attempts = 0
                    yield from bot.Wait._coro_for_time(max(50, int(retry_delay_ms)))
                    continue

                debug_log_fn(
                    f"{name}: retrying waypoint {point_i + 1}/{len(path_points)} "
                    f"(attempt={attempts}, dist={distance:.0f}, tol={float(arrival_tolerance):.0f})"
                )
                yield from bot.Wait._coro_for_time(max(50, int(retry_delay_ms)))

    if pause_on_combat:
        bot.States.AddCustomState(
            lambda: bot.Properties.ApplyNow("pause_on_danger", "active", True),
            f"{name}: Enable Pause On Combat",
        )

    bot.States.AddCustomState(_run_auto_path, str(name))

    if pause_on_combat:
        bot.States.AddCustomState(
            lambda was_active=bool(pause_on_danger_was_active): bot.Properties.ApplyNow(
                "pause_on_danger", "active", was_active
            ),
            f"{name}: Restore Pause On Combat",
        )


def add_auto_path_delayed_state(
    bot,
    *,
    points: Iterable[tuple[float, float]],
    name: str,
    delay_ms: int,
) -> None:
    path_points = [(float(x), float(y)) for x, y in points]
    delay = max(0, int(delay_ms))

    def _run_delayed_path():
        for point_i, (x, y) in enumerate(path_points):
            if cutscene_active():
                return
            step_name = f"{name} [{point_i + 1}/{len(path_points)}]"
            yield from bot.Move._coro_xy(float(x), float(y), step_name=step_name)
            if cutscene_active():
                return
            if point_i < len(path_points) - 1 and delay > 0:
                yield from bot.Wait._coro_for_time(delay)

    bot.States.AddCustomState(_run_delayed_path, str(name))


def add_patrol_until_enemy_state(
    bot,
    *,
    points: Iterable[tuple[float, float]],
    enemy_resolver: EnemyResolver,
    name: str,
    set_target: bool = False,
    point_wait_ms: int = 0,
    lap_wait_ms: int = 0,
    max_laps: int = 0,
    timeout_ms: int = 0,
    log: LogFn | None = None,
) -> None:
    from Py4GWCoreLib import Player

    path_points = [(float(x), float(y)) for x, y in points]
    log_fn = log or _noop_log

    def _patrol_until_enemy():
        started_at = monotonic()
        completed_laps = 0

        while True:
            if cutscene_active():
                return
            detected_enemy = enemy_resolver()
            if detected_enemy is not None:
                if set_target:
                    Player.ChangeTarget(int(detected_enemy))
                return
            if timeout_ms > 0 and (monotonic() - started_at) * 1000.0 >= timeout_ms:
                log_fn(f"{name}: timeout reached without detecting enemies.")
                return
            if max_laps > 0 and completed_laps >= max_laps:
                log_fn(f"{name}: max_laps reached without detecting enemies.")
                return

            for point_idx, (x, y) in enumerate(path_points):
                yield from bot.Move._coro_xy(
                    float(x),
                    float(y),
                    f"{name} [{completed_laps + 1}.{point_idx + 1}]",
                    fail_on_unmanaged=False,
                )
                if cutscene_active():
                    return
                detected_enemy = enemy_resolver()
                if detected_enemy is not None:
                    if set_target:
                        Player.ChangeTarget(int(detected_enemy))
                    return
                if point_wait_ms > 0:
                    yield from bot.Wait._coro_for_time(int(point_wait_ms))

            completed_laps += 1
            if lap_wait_ms > 0:
                yield from bot.Wait._coro_for_time(int(lap_wait_ms))

    bot.States.AddCustomState(_patrol_until_enemy, str(name))


def add_aggro_path_state(
    bot,
    *,
    points: Iterable[tuple[float, float]],
    name: str,
    detection_radius: float = 2500.0,
    clear_radius: float = 2500.0,
    arrival_tolerance: float = 150.0,
    scan_interval_ms: int = 500,
    scan_move_ratio: float = 0.75,
    stop_when_vanquished: bool = False,
    log_stats: bool = False,
    stats_interval_ms: int = 30_000,
    on_enemy_detected: Callable[[float, float], None] | None = None,
    log: LogFn | None = None,
) -> None:
    from Py4GWCoreLib import Agent, AgentArray, Console, ConsoleLog, GLOBAL_CACHE, Map, Player, Range, Routines, Utils
    from Py4GWCoreLib.Pathing import AutoPathing

    path_points = [(float(x), float(y)) for x, y in points]
    log_fn = log or _noop_log
    detect_radius = max(1.0, float(detection_radius or 2500.0))
    chase_clear_radius = max(detect_radius, float(clear_radius or detect_radius))
    tolerance = max(25.0, float(arrival_tolerance or 150.0))
    engage_radius = float(getattr(Range, "Spellcast", Range.Earshot).value)
    scan_ms = max(50, int(scan_interval_ms or 500))
    scan_move_threshold = detect_radius * max(0.05, float(scan_move_ratio or 0.75))
    stats_ms = max(1000, int(stats_interval_ms or 30_000))

    def _is_player_dead() -> bool:
        try:
            player_id = int(Player.GetAgentID() or 0)
            return bool(player_id and Agent.IsDead(player_id))
        except Exception:
            return False

    def _recovery_blocking() -> bool:
        try:
            return bool(_is_player_dead() or Routines.Checks.Party.IsPartyWiped() or GLOBAL_CACHE.Party.IsPartyDefeated())
        except Exception:
            return _is_player_dead()

    def _vanquish_done() -> bool:
        try:
            return bool(stop_when_vanquished and Map.IsVanquishCompleted())
        except Exception:
            return False

    def _map_signature() -> tuple[int, bool]:
        try:
            return (int(Map.GetMapID() or 0), bool(Map.IsMapLoading()))
        except Exception:
            return (0, True)

    def _aggro_path():
        if not path_points:
            return

        start_map_id, _ = _map_signature()
        mode = "path"
        point_idx = 0
        current_enemy: int | None = None
        last_scanned_enemy: int | None = None
        last_scan_pos = Player.GetXY()
        last_scan_at = 0.0
        last_target_id: int | None = None
        last_move_target: tuple[int, int] | None = None
        last_path_move: tuple[int, int] | None = None
        last_path_move_at = 0.0
        stats_started_at = monotonic()
        enemy_array_fetches = 0
        change_target_calls = 0
        move_calls = 0

        def _map_changed_or_unavailable() -> bool:
            current_map_id, is_loading = _map_signature()
            return bool(is_loading or not current_map_id or (start_map_id and current_map_id != start_map_id))

        def _find_nearest_enemy(radius: float) -> int | None:
            nonlocal enemy_array_fetches
            enemy_array_fetches += 1
            player_xy = Player.GetXY()
            return select_nearest_alive_enemy(
                AgentArray.GetEnemyArray(),
                player_xy=player_xy,
                max_distance=float(radius),
                is_alive=lambda agent_id: bool(Agent.IsAlive(agent_id)),
                get_xy=lambda agent_id: Agent.GetXY(agent_id),
                distance=lambda left, right: Utils.Distance(left, right),
            )

        def _throttled_scan(radius: float) -> int | None:
            nonlocal last_scanned_enemy, last_scan_pos, last_scan_at
            now = monotonic()
            curr_pos = Player.GetXY()
            dist_moved = Utils.Distance(curr_pos, last_scan_pos)
            interval_elapsed = (now - last_scan_at) * 1000.0 >= scan_ms
            if last_scan_at <= 0.0 or dist_moved >= scan_move_threshold or interval_elapsed:
                last_scanned_enemy = _find_nearest_enemy(radius)
            last_scan_pos = curr_pos
            last_scan_at = now
            return last_scanned_enemy

        def _move_to_xy(x: float, y: float, *, dedupe: bool = True) -> None:
            nonlocal last_move_target, move_calls
            next_move = (int(x), int(y))
            if dedupe and next_move == last_move_target:
                return
            Player.Move(float(x), float(y))
            move_calls += 1
            last_move_target = next_move

        def _valid_alive_enemy(agent_id: int | None) -> bool:
            try:
                return bool(agent_id is not None and Agent.IsValid(int(agent_id)) and Agent.IsAlive(int(agent_id)))
            except Exception:
                return False

        def _chase_enemy(agent_id: int):
            nonlocal current_enemy, last_move_target
            try:
                target_x, target_y = Agent.GetXY(agent_id)
                player_x, player_y = Player.GetXY()
                player_agent = Player.GetAgent()
                zplane = float(getattr(getattr(player_agent, "pos", None), "zplane", 0.0) or 0.0)
            except Exception:
                current_enemy = None
                return

            if Utils.Distance((player_x, player_y), (target_x, target_y)) <= engage_radius:
                try:
                    Player.Interact(int(agent_id), False)
                except Exception:
                    pass
                yield from bot.Wait._coro_for_time(250)
                return

            chase_path = yield from AutoPathing().get_path(
                (float(player_x), float(player_y), zplane),
                (float(target_x), float(target_y), zplane),
                smooth_by_los=True,
                margin=100,
                step_dist=200.0,
                smooth_by_chaikin=False,
            )
            chase_points = [(float(pt[0]), float(pt[1])) for pt in (chase_path or [])]
            if len(chase_points) <= 1:
                chase_points = [(float(target_x), float(target_y))]

            for chase_x, chase_y in chase_points[1:9]:
                if cutscene_active() or _map_changed_or_unavailable() or _vanquish_done():
                    return
                if _recovery_blocking():
                    return
                rescanned = _throttled_scan(chase_clear_radius)
                if rescanned is not None and rescanned != agent_id:
                    current_enemy = rescanned
                    last_move_target = None
                    return
                if not _valid_alive_enemy(agent_id):
                    current_enemy = None
                    return

                _move_to_xy(chase_x, chase_y)
                started_at = monotonic()
                while Utils.Distance(Player.GetXY(), (chase_x, chase_y)) > tolerance:
                    if cutscene_active() or _map_changed_or_unavailable() or _vanquish_done():
                        return
                    if _recovery_blocking():
                        return
                    nearby = _throttled_scan(chase_clear_radius)
                    if nearby is not None and nearby != agent_id:
                        current_enemy = nearby
                        last_move_target = None
                        return
                    if (monotonic() - started_at) * 1000.0 >= 1500:
                        break
                    yield from bot.Wait._coro_for_time(150)

        def _maybe_log_stats() -> None:
            nonlocal stats_started_at, enemy_array_fetches, change_target_calls, move_calls
            if not log_stats:
                return
            elapsed_ms = (monotonic() - stats_started_at) * 1000.0
            if elapsed_ms < stats_ms:
                return
            ConsoleLog(
                "AggroPath",
                (
                    f"{name}: stats over {int(elapsed_ms / 1000)}s "
                    f"fetches={enemy_array_fetches}, changeTarget={change_target_calls}, move={move_calls}"
                ),
                Console.MessageType.Info,
                log=True,
            )
            stats_started_at = monotonic()
            enemy_array_fetches = 0
            change_target_calls = 0
            move_calls = 0

        log_fn(f"{name}: starting aggro path ({len(path_points)} pts, detect={detect_radius:.0f}, clear={chase_clear_radius:.0f}).")
        while point_idx < len(path_points):
            if cutscene_active() or _map_changed_or_unavailable() or _vanquish_done():
                return
            while _recovery_blocking():
                if cutscene_active() or _map_changed_or_unavailable() or _vanquish_done():
                    return
                yield from bot.Wait._coro_for_time(1000)

            _maybe_log_stats()

            if mode == "path":
                detected_enemy = _throttled_scan(detect_radius)
                if detected_enemy is not None:
                    current_enemy = detected_enemy
                    mode = "combat"
                    last_move_target = None
                    last_scanned_enemy = None
                    if on_enemy_detected is not None:
                        ex, ey = Agent.GetXY(detected_enemy)
                        on_enemy_detected(float(ex), float(ey))
                    continue

                target_x, target_y = path_points[point_idx]
                dist_to_waypoint = Utils.Distance(Player.GetXY(), (target_x, target_y))
                if dist_to_waypoint <= tolerance:
                    point_idx += 1
                    last_path_move = None
                    continue

                now = monotonic()
                next_path_move = (int(target_x), int(target_y))
                if last_path_move != next_path_move or (now - last_path_move_at) * 1000.0 >= 2000:
                    Player.Move(float(target_x), float(target_y))
                    move_calls += 1
                    last_path_move = next_path_move
                    last_path_move_at = now
                yield from bot.Wait._coro_for_time(250)
                continue

            if current_enemy is None or not Agent.IsValid(current_enemy) or not Agent.IsAlive(current_enemy):
                current_enemy = _find_nearest_enemy(chase_clear_radius)
                if current_enemy is None:
                    mode = "path"
                    last_move_target = None
                    continue

            rescanned_enemy = _throttled_scan(chase_clear_radius)
            if rescanned_enemy is None:
                mode = "path"
                current_enemy = None
                last_move_target = None
                continue

            current_enemy = rescanned_enemy
            if current_enemy != last_target_id:
                Player.ChangeTarget(current_enemy)
                change_target_calls += 1
                last_target_id = current_enemy

            yield from _chase_enemy(current_enemy)

        log_fn(f"{name}: aggro path complete.")

    bot.States.AddCustomState(_aggro_path, str(name))


def add_auto_path_till_timeout_state(
    bot,
    *,
    points: Iterable[tuple[float, float]],
    name: str,
    timeout_ms: int,
    point_wait_ms: int = 0,
    lap_wait_ms: int = 0,
    log: LogFn | None = None,
) -> None:
    path_points = [(float(x), float(y)) for x, y in points]
    log_fn = log or _noop_log

    def _run_until_timeout():
        if timeout_ms <= 0:
            log_fn(f"{name}: timeout_ms <= 0, skipping.")
            return

        started_at = monotonic()
        lap_idx = 0
        while True:
            if cutscene_active():
                return
            elapsed_ms = (monotonic() - started_at) * 1000.0
            if elapsed_ms >= timeout_ms:
                return

            for point_idx, (x, y) in enumerate(path_points):
                elapsed_ms = (monotonic() - started_at) * 1000.0
                if elapsed_ms >= timeout_ms:
                    return
                remaining_ms = max(1, int(timeout_ms - elapsed_ms))
                yield from bot.Move._coro_xy(
                    float(x),
                    float(y),
                    f"{name} [{lap_idx + 1}.{point_idx + 1}]",
                    forced_timeout=remaining_ms,
                    fail_on_unmanaged=False,
                )
                if cutscene_active():
                    return
                elapsed_ms = (monotonic() - started_at) * 1000.0
                if elapsed_ms >= timeout_ms:
                    return
                if point_wait_ms > 0:
                    wait_ms = min(int(point_wait_ms), max(0, int(timeout_ms - elapsed_ms)))
                    if wait_ms > 0:
                        yield from bot.Wait._coro_for_time(wait_ms)

            lap_idx += 1
            if lap_wait_ms > 0:
                elapsed_ms = (monotonic() - started_at) * 1000.0
                if elapsed_ms >= timeout_ms:
                    return
                wait_ms = min(int(lap_wait_ms), max(0, int(timeout_ms - elapsed_ms)))
                if wait_ms > 0:
                    yield from bot.Wait._coro_for_time(wait_ms)

    bot.States.AddCustomState(_run_until_timeout, str(name))
