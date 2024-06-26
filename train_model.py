# src/train_model.py

import tensorflow as tf
from data_loader import load_mnist_data

def build_model():
    model = tf.keras.models.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(10, activation='softmax')
    ])
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model

def train_model():
    (x_train, y_train), (x_test, y_test) = load_mnist_data()
    model = build_model()
    model.fit(x_train, y_train, epochs=5)
    model.evaluate(x_test, y_test)
    model.save('models/mnist_model.h5')

if __name__ == '__main__':
    train_model()
