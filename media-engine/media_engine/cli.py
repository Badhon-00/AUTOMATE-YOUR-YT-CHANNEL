from __future__ import annotations
import argparse
import json
from .processor import process_audio

def main() -> None:
    parser = argparse.ArgumentParser(description="Rights-aware local music audio processor")
    commands = parser.add_subparsers(dest="command", required=True)
    process = commands.add_parser("process", help="Create a slowed/reverb derivative")
    process.add_argument("--input", required=True)
    process.add_argument("--manifest", required=True)
    process.add_argument("--output", required=True)
    process.add_argument("--speed", type=float, default=0.88)
    process.add_argument("--reverb", type=int, default=45)
    args = parser.parse_args()
    if args.command == "process":
        result = process_audio(args.input, args.manifest, args.output, args.speed, args.reverb)
        print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
