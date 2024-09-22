import os
import argparse

ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".gif"}


def remove_invalid_files(root_dir: str, dry_run: bool = False) -> int:
    removed = 0

    for subdir, _, files in os.walk(root_dir):
        for file in files:
            ext = os.path.splitext(file)[-1].lower()
            if ext not in ALLOWED_EXTENSIONS:
                path = os.path.join(subdir, file)
                print(f"❌ Removing (unsupported ext): {path}")
                if not dry_run:
                    os.remove(path)
                removed += 1

    return removed


def main():
    parser = argparse.ArgumentParser(description="Delete non-image files from dataset folders.")
    parser.add_argument("--root", default="data", help="Root dataset directory (default: data)")
    parser.add_argument("--dry-run", action="store_true", help="Print only, do not delete")
    args = parser.parse_args()

    print(f"🔍 Scanning: {args.root}")
    removed = remove_invalid_files(args.root, dry_run=args.dry_run)
    print(f"✅ Done. Removed {removed} files.")


if __name__ == "__main__":
    main()
