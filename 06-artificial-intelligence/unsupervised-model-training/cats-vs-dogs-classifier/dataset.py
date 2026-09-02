import tensorflow as tf


def load_data():

    train = tf.keras.utils.image_dataset_from_directory(
        "data/train",
        image_size=(150,150),
        batch_size=32,
        label_mode="binary"
    )


    validation = tf.keras.utils.image_dataset_from_directory(
        "data/validation",
        image_size=(150,150),
        batch_size=32,
        label_mode="binary"
    )


    return train, validation