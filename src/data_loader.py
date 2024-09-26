import tensorflow as tf

IMG_SIZE = (224, 224)
BATCH_SIZE = 32


def get_datasets(train_dir: str, val_dir: str, test_dir: str):
    train_ds = tf.keras.utils.image_dataset_from_directory(
        train_dir,
        label_mode="categorical",
        image_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        shuffle=True,
    )

    val_ds = tf.keras.utils.image_dataset_from_directory(
        val_dir,
        label_mode="categorical",
        image_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        shuffle=False,
    )

    test_ds = tf.keras.utils.image_dataset_from_directory(
        test_dir,
        label_mode="categorical",
        image_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        shuffle=False,
    )

    return train_ds, val_ds, test_ds


def with_prefetch(ds: tf.data.Dataset) -> tf.data.Dataset:
    return ds.prefetch(buffer_size=tf.data.AUTOTUNE)
