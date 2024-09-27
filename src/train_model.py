import os
import argparse
import tensorflow as tf
from tensorflow.keras import layers, models

from data_loader import get_datasets, with_prefetch


def build_model(num_classes: int) -> tf.keras.Model:
    base_model = tf.keras.applications.MobileNetV2(
        input_shape=(224, 224, 3),
        include_top=False,
        weights="imagenet",
    )
    base_model.trainable = False

    model = models.Sequential(
        [
            layers.Input(shape=(224, 224, 3)),
            tf.keras.applications.mobilenet_v2.preprocess_input,
            base_model,
            layers.GlobalAveragePooling2D(),
            layers.Dropout(0.2),
            layers.Dense(num_classes, activation="softmax"),
        ]
    )

    model.compile(
        optimizer=tf.keras.optimizers.Adam(),
        loss="categorical_crossentropy",
        metrics=["accuracy"],
    )
    return model


def main():
    parser = argparse.ArgumentParser(description="Train waste classifier (MobileNetV2 transfer learning).")
    parser.add_argument("--train", default="data/train")
    parser.add_argument("--val", default="data/val")
    parser.add_argument("--test", default="data/test")
    parser.add_argument("--epochs", type=int, default=10)
    parser.add_argument("--out", default="models/mobilenet_waste_classifier.h5")
    args = parser.parse_args()

    os.makedirs(os.path.dirname(args.out), exist_ok=True)

    train_ds, val_ds, test_ds = get_datasets(args.train, args.val, args.test)
    train_ds = with_prefetch(train_ds)
    val_ds = with_prefetch(val_ds)
    test_ds = with_prefetch(test_ds)

    num_classes = len(train_ds.class_names)
    model = build_model(num_classes=num_classes)

    model.fit(
        train_ds,
        validation_data=val_ds,
        epochs=args.epochs,
    )

    test_loss, test_acc = model.evaluate(test_ds, verbose=0)
    print(f"🧪 Test accuracy: {test_acc:.4f}, loss: {test_loss:.4f}")

    model.save(args.out)
    print(f"✅ Saved model: {args.out}")


if __name__ == "__main__":
    main()
