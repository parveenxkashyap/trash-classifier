import argparse
import numpy as np
import tensorflow as tf
from sklearn.metrics import classification_report, confusion_matrix


def main():
    parser = argparse.ArgumentParser(description="Evaluate a trained classifier on the test dataset.")
    parser.add_argument("--model", default="models/mobilenet_waste_classifier.h5")
    parser.add_argument("--test", default="data/test")
    parser.add_argument("--batch-size", type=int, default=32)
    args = parser.parse_args()

    model = tf.keras.models.load_model(args.model)

    test_ds = tf.keras.utils.image_dataset_from_directory(
        args.test,
        image_size=(224, 224),
        batch_size=args.batch_size,
        shuffle=False,
        label_mode="int",
    )

    class_names = test_ds.class_names

    y_true = np.concatenate([y for _, y in test_ds], axis=0)
    y_pred_probs = model.predict(test_ds)
    y_pred = np.argmax(y_pred_probs, axis=1)

    print("\n📊 Classification Report:\n")
    print(classification_report(y_true, y_pred, target_names=class_names))

    print("\n🧱 Confusion Matrix:\n")
    print(confusion_matrix(y_true, y_pred))


if __name__ == "__main__":
    main()
