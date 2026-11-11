from __future__ import annotations
import json
import shutil
import subprocess
from pathlib import Path
from .rights import validate_rights

class MediaError(RuntimeError):
    """Raised when FFmpeg cannot process the requested media."""

def _run(args: list[str]) -> str:
    result = subprocess.run(args, check=False, capture_output=True, text=True)
    if result.returncode:
        raise MediaError(result.stderr[-2000:] or "Media command failed")
    return result.stdout

def probe(path: str | Path) -> dict:
    raw = _run(["ffprobe", "-v", "error", "-show_entries",
                "format=duration:stream=codec_type,sample_rate,channels",
                "-of", "json", str(path)])
    return json.loads(raw)

def process_audio(input_path: str, manifest_path: str, output_path: str,
                  speed: float = 0.88, reverb: int = 45) -> dict:
    if not shutil.which("ffmpeg") or not shutil.which("ffprobe"):
        raise MediaError("FFmpeg and ffprobe must be installed and available on PATH.")
    if not 0.70 <= speed <= 1.0:
        raise ValueError("speed must be between 0.70 and 1.0")
    if not 0 <= reverb <= 100:
        raise ValueError("reverb must be between 0 and 100")
    validate_rights(manifest_path, input_path)
    source_info = probe(input_path)
    if not any(s.get("codec_type") == "audio" for s in source_info.get("streams", [])):
        raise MediaError("Input contains no audio stream.")
    destination = Path(output_path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    delay = max(1, int(35 * reverb / 100))
    decay = 0.15 + (0.45 * reverb / 100)
    filters = (f"atempo={speed},"
               f"aecho=0.8:0.7:{delay}|{delay * 2}:{decay}|{decay / 2},"
               "loudnorm=I=-14:TP=-1.0:LRA=11")
    _run(["ffmpeg", "-y", "-i", input_path, "-vn", "-af", filters,
          "-c:a", "pcm_s24le", str(destination)])
    rendered_info = probe(destination)
    return {"output": str(destination), "source": source_info,
            "rendered": rendered_info, "settings": {"speed": speed, "reverb": reverb}}
