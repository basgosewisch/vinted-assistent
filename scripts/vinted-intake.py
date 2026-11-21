#!/usr/bin/env python3
"""Collect selected Vinted photos without changing the originals."""

import argparse
import fcntl
import hashlib
import json
import os
from pathlib import Path
import tempfile


IMAGE_EXTENSIONS = {".avif", ".heic", ".heif", ".jpeg", ".jpg", ".png", ".webp"}
DEFAULT_STATE_DIR = Path(__file__).resolve().parent / "work" / "vinted-intake"


def is_image_file(path):
    return path.is_file() and path.suffix.lower() in IMAGE_EXTENSIONS


def fingerprint(path):
    stat = path.stat()
    return [stat.st_size, stat.st_mtime_ns]


def downloads_snapshot(directory):
    files = {}
    for path in directory.iterdir():
        if is_image_file(path) and not path.name.startswith("."):
            try:
                files[path.name] = fingerprint(path)
            except FileNotFoundError:
                continue
    return files


def write_atomic(path, data):
    with tempfile.NamedTemporaryFile(dir=path.parent, delete=False) as temporary:
        try:
            temporary.write(data)
            temporary.close()
            os.replace(temporary.name, path)
        finally:
            Path(temporary.name).unlink(missing_ok=True)


def stage_photo(path, asset_dir):
    before = fingerprint(path)
    contents = path.read_bytes()
    if not contents or before != fingerprint(path):
        raise ValueError(f"Bestand is leeg of nog in gebruik: {path}")
    key = hashlib.sha256(contents).hexdigest()
    existing = next(asset_dir.glob(f"{key}.*"), None)
    target = existing or asset_dir / f"{key}{path.suffix.lower()}"
    if existing is None:
        write_atomic(target, contents)
    return {"bron": str(path), "foto": str(target), "dubbel": existing is not None}, before


def run(args):
    downloads = args.downloads.expanduser().resolve()
    directory = args.state_dir.expanduser().resolve()
    directory.mkdir(parents=True, exist_ok=True)
    state_path = directory / "downloads.json"

    with (directory / ".lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        if args.command == "baseline":
            if state_path.exists():
                raise ValueError("De Downloads-nulmeting bestaat al.")
            snapshot = downloads_snapshot(downloads)
            write_atomic(state_path, json.dumps(snapshot).encode())
            return {"bestanden_in_nulmeting": len(snapshot)}

        if not state_path.exists():
            raise ValueError("Leg eerst de Downloads-nulmeting vast met baseline.")
        seen = json.loads(state_path.read_text())
        if args.command == "scan":
            current = downloads_snapshot(downloads)
            paths = sorted(current, key=lambda name: (current[name][1], name))
            return [str(downloads / name) for name in paths if seen.get(name) != current[name]]

        paths = [Path(value).expanduser().resolve(strict=True) for value in args.paths]
        for path in paths:
            if not is_image_file(path):
                raise ValueError(f"Geen ondersteund fotobestand: {path}")
            if args.command == "ignore" and path.parent != downloads:
                raise ValueError(f"Bestand staat buiten Downloads: {path}")

        results = []
        if args.command == "stage":
            assets = directory / "photos"
            assets.mkdir(exist_ok=True)
            for path in paths:
                result, signature = stage_photo(path, assets)
                results.append(result)
                if path.parent == downloads:
                    seen[path.name] = signature
        else:
            for path in paths:
                seen[path.name] = fingerprint(path)
                results.append(str(path))
        write_atomic(state_path, json.dumps(seen).encode())
        return results


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--downloads", type=Path, default=Path.home() / "Downloads")
    parser.add_argument("--state-dir", type=Path, default=DEFAULT_STATE_DIR)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("baseline")
    commands.add_parser("scan")
    commands.add_parser("stage").add_argument("paths", nargs="+")
    commands.add_parser("ignore").add_argument("paths", nargs="+")
    try:
        result = run(parser.parse_args())
    except (OSError, ValueError) as exc:
        parser.exit(1, f"{exc}\n")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
