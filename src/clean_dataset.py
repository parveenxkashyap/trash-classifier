import os
import argparse
from PIL import Image

VALID_EXTENSIONS = (".jpg", ".jpeg", ".png", ".bmp", ".gif")


def clean_directory(directory: str, dry_run: bool = False) -> dict:
    stats = {
        "unsupported_deleted": 0,
        "corrupt_deleted": 0,
        "scanned": 0,
    }

    print(f"📂 Scanning: {directory}")

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            stats["scanned"] += 1

            if not file.lower().endswith(VALID_EXTENSIONS):
                print(f"❌ Deleting unsupported file: {file_path}")
                if not dry_run:
                    os.remove(file_path)
                stats["unsupported_deleted"] += 1
                continue

            try:
                with Image.open(file_path) as img:
                    img.verify()
            except Exception as e:
                print(f"⚠️ Corrupt image deleted: {file_path} | Error: {e}")
                if not dry_run:
                    os.remove(file_path)
                stats["corrupt_deleted"] += 1

    return stats


def main():
    parser = argparse.ArgumentParser(description="Clean dataset by extension + PIL verification.")
    parser.add_argument(
        "--folders",
        nargs="*",
        default=["data/train", "data/val", "data/test"],
        help="Folders to clean (default: data/train data/val data/test)",
    )
    parser.add_argument("--dry-run", action="store_true", help="Print only, do not delete")
    args = parser.parse_args()

    total = {"unsupported_deleted": 0, "corrupt_deleted": 0, "scanned": 0}
    for folder in args.folders:
        if not os.path.exists(folder):
            continue
        s = clean_directory(folder, dry_run=args.dry_run)
        for k in total:
            total[k] += s[k]

    print(
        f"✅ Done. Scanned={total['scanned']}, "
        f"unsupported_deleted={total['unsupported_deleted']}, "
        f"corrupt_deleted={total['corrupt_deleted']}"
    )


if __name__ == "__main__":
    main()
