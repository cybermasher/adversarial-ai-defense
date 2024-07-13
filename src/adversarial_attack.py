# src/adversarial_attack.py

import tensorflow as tf
import numpy as np
from functools import lru_cache

@lru_cache(maxsize=1)
def load_mnist_data():
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
    x_train, x_test = x_train / 255.0, x_test / 255.0
    return (x_train, y_train), (x_test, y_test)

def create_adversarial_pattern(model, image, label):
    with tf.GradientTape() as tape:
        tape.watch(image)
        prediction = model(image)
        loss = tf.keras.losses.sparse_categorical_crossentropy(label, prediction)
    gradient = tape.gradient(loss, image)
    signed_grad = tf.sign(gradient)
    return signed_grad

def generate_adversarial_examples():
    (x_train, y_train), (x_test, y_test) = load_mnist_data()
    model = tf.keras.models.load_model('models/mnist_model.h5')

    x_test = x_test[:100]
    y_test = y_test[:100]

    perturbations = create_adversarial_pattern(model, x_test, y_test)
    epsilon = 0.1
    x_test_adversarial = x_test + epsilon * perturbations
    return x_test, x_test_adversarial, y_test

if __name__ == '__main__':
    original, adversarial, labels = generate_adversarial_examples()
    np.save('data/original.npy', original)
    np.save('data/adversarial.npy', adversarial)
    np.save('data/labels.npy', labels)
