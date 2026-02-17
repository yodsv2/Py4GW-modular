from __future__ import annotations

from pathlib import Path


def get_botting_base_dir() -> Path:
    """
    Resolve the `Py4GWCoreLib/botting_src` directory without relying solely on __file__.
    Priority:
    1) Py4GW project path (runtime-safe in embedded environment)
    2) CWD heuristics
    3) __file__ fallback
    """
    # 1) Preferred: runtime project path from Py4GW console.
    try:
        import Py4GW  # type: ignore

        project_path = Path(Py4GW.Console.get_projects_path())
        candidate = project_path / "Py4GWCoreLib" / "botting_src"
        if candidate.exists():
            return candidate
    except Exception:
        pass

    # 2) CWD heuristics.
    cwd = Path.cwd()
    candidate = cwd / "Py4GWCoreLib" / "botting_src"
    if candidate.exists():
        return candidate

    candidate = cwd / "botting_src"
    if candidate.exists():
        return candidate

    # 3) Final fallback: this module location.
    try:
        return Path(__file__).resolve().parent.parent
    except Exception as exc:
        raise RuntimeError("Unable to resolve botting_src directory") from exc


def get_scenarios_dir() -> Path:
    return get_botting_base_dir() / "scenarios"

