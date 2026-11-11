from __future__ import annotations
import json
from pathlib import Path

class RightsError(ValueError):
    """Raised when a source track lacks required documented permissions."""

def validate_rights(manifest_path: str | Path, input_path: str | Path) -> dict:
    data = json.loads(Path(manifest_path).read_text(encoding="utf-8"))
    tracks = data.get("tracks", [])
    target = Path(input_path).name
    match = next((item for item in tracks if Path(item.get("file", "")).name == target), None)
    if match is None:
        raise RightsError(f"No rights record matches {target!r}.")
    required = ("commercial_use", "derivative_works", "permission_evidence")
    missing = [key for key in required if not match.get(key)]
    if missing:
        raise RightsError("Missing rights confirmations: " + ", ".join(missing))
    return match
