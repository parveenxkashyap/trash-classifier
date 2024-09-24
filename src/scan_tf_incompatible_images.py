import os
import argparse
import tensorflow as tf


def is_tf_compatible_image(path: str) -> bool:
    try:
        img_raw = tf.io.read_file(path)
        _ = tf.image.decode_image(img_raw)
        return True
    except (tf.errors.InvalidArgumentError, ValueError):
        return False


def scan_images(root_dir: str, delete: bool = False) -> int:
    bad_images = []

    for root, _, files in os.walk(root_dir):
        for file in files:
            file_path = os.path.join(root, file)

            if not is_tf_compatible_image(file_path):
                print(f"❌ Invalid TensorFlow image: {file_path}")
                bad_images.append(file_path)

    print(f"\n✅ Scan complete. Found {len(bad_images)} incompatible images.")

    if delete:
        for path in bad_images:
            os.remove(path)
            print(f"🗑️ Deleted: {path}")

    return len(bad_images)


def main():
    parser = argparse.ArgumentParser(description="Scan images that TensorFlow cannot decode.")
    parser.add_argument("--root", default="data", help="Root dataset directory (default: data)")
    parser.add_argument("--delete", action="store_true", help="Delete incompatible files")
    args = parser.parse_args()

    scan_images(args.root, delete=args.delete)


if __name__ == "__main__":
    main()
