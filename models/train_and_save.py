# train_and_save_model.py

import tensorflow as tf
from tensorflow.keras.datasets import mnist

def load_mnist_data():
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train, x_test = x_train / 255.0, x_test / 255.0
    return (x_train, y_train), (x_test, y_test)

def build_model():
    model = tf.keras.models.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(10, activation='softmax')
    ])
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model

def train_and_save_model():
    (x_train, y_train), (x_test, y_test) = load_mnist_data()
    model = build_model()
    model.fit(x_train, y_train, epochs=5)
    model.save('mnist_model.h5')
    print("Model saved as 'mnist_model.h5'")

if __name__ == '__main__':
    train_and_save_model()
