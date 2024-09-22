import os
import shutil
import argparse
from sklearn.model_selection import train_test_split


def split_dataset(
    source_dir: str,
    train_dir: str,
    val_dir: str,
    test_dir: str,
    val_ratio: float = 0.15,
    test_ratio: float = 0.15,
    seed: int = 42,
) -> None:
    if val_ratio + test_ratio >= 1.0:
        raise ValueError("val_ratio + test_ratio must be < 1.0")

    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(val_dir, exist_ok=True)
    os.makedirs(test_dir, exist_ok=True)

    categories = [
        d for d in os.listdir(source_dir)
        if os.path.isdir(os.path.join(source_dir, d))
    ]

    for category in categories:
        category_path = os.path.join(source_dir, category)
        images = [
            f for f in os.listdir(category_path)
            if os.path.isfile(os.path.join(category_path, f))
        ]

        train_imgs, temp_imgs = train_test_split(
            images, test_size=(val_ratio + test_ratio), random_state=seed
        )
        val_imgs, test_imgs = train_test_split(
            temp_imgs,
            test_size=test_ratio / (val_ratio + test_ratio),
            random_state=seed,
        )

        splits = [
            (train_dir, train_imgs),
            (val_dir, val_imgs),
            (test_dir, test_imgs),
        ]

        for out_dir, image_list in splits:
            out_category_dir = os.path.join(out_dir, category)
            os.makedirs(out_category_dir, exist_ok=True)

            for img in image_list:
                src = os.path.join(category_path, img)
                dst = os.path.join(out_category_dir, img)
                shutil.copy2(src, dst)


def main():
    parser = argparse.ArgumentParser(description="Split a folder dataset into train/val/test.")
    parser.add_argument("--source", default="data/raw/garbage-dataset")
    parser.add_argument("--train", default="data/train")
    parser.add_argument("--val", default="data/val")
    parser.add_argument("--test", default="data/test")
    parser.add_argument("--val-ratio", type=float, default=0.15)
    parser.add_argument("--test-ratio", type=float, default=0.15)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    split_dataset(
        source_dir=args.source,
        train_dir=args.train,
        val_dir=args.val,
        test_dir=args.test,
        val_ratio=args.val_ratio,
        test_ratio=args.test_ratio,
        seed=args.seed,
    )
    print("✅ Dataset split complete.")


if __name__ == "__main__":
    main()
