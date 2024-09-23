import os
import argparse
from PIL import Image


def is_image_valid(filepath: str) -> bool:
    try:
        with Image.open(filepath) as img:
            img.verify()
        return True
    except Exception:
        return False


def clean_directory(root_dir: str, dry_run: bool = False) -> int:
    print(f"🔍 Checking images in: {root_dir}")
    bad_files = 0

    for subdir, _, files in os.walk(root_dir):
        for file in files:
            filepath = os.path.join(subdir, file)
            if not is_image_valid(filepath):
                print(f"❌ Removing invalid image: {filepath}")
                if not dry_run:
                    os.remove(filepath)
                bad_files += 1

    print(f"✅ Finished. Removed {bad_files} invalid images from {root_dir}.")
    return bad_files


def main():
    parser = argparse.ArgumentParser(description="Strictly validate images using PIL verify().")
    parser.add_argument(
        "--folders",
        nargs="*",
        default=["data/train", "data/val", "data/test"],
        help="Folders to validate (default: data/train data/val data/test)",
    )
    parser.add_argument("--dry-run", action="store_true", help="Print only, do not delete")
    args = parser.parse_args()

    total = 0
    for folder in args.folders:
        if os.path.exists(folder):
            total += clean_directory(folder, dry_run=args.dry_run)

    print(f"✅ Total invalid images removed: {total}")


if __name__ == "__main__":
    main()
