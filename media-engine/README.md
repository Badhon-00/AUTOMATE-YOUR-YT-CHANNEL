# Rights-aware music media engine

A local-only FFmpeg processing starter for audio files that you own or are licensed to adapt.

## Requirements
- Python 3.11+
- FFmpeg and ffprobe on PATH

## Rights manifest
Copy `examples/rights-manifest.example.json` and add a record matching the input filename. The processor refuses to run unless commercial use, derivative-work permission, and a permission-evidence reference are present.

## Example
```bash
cd media-engine
python -m media_engine.cli process --input ./licensed-track.wav --manifest ./rights.json --output ./output/slowed-reverb.wav --speed 0.88 --reverb 45
python -m unittest discover -s tests
```

The tool does not download music, bypass DRM/Content ID, upload to YouTube, or predict copyright claims. A transformation does not grant rights.
