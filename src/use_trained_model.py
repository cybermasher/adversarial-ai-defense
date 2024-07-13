# src/use_trained_model.py

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
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

def generate_adversarial_examples(model):
    (x_train, y_train), (x_test, y_test) = load_mnist_data()
    x_test = x_test[:100]
    y_test = y_test[:100]
    perturbations = create_adversarial_pattern(model, x_test, y_test)
    epsilon = 0.1
    x_test_adversarial = x_test + epsilon * perturbations
    return x_test, x_test_adversarial, y_test

def load_and_evaluate_model():
    model = tf.keras.models.load_model('models/mnist_model.h5')
    (x_train, y_train), (x_test, y_test) = load_mnist_data()

    loss, acc = model.evaluate(x_test, y_test)
    print(f"Model accuracy on clean examples: {acc * 100:.2f}%")

    x_test, x_test_adversarial, y_test = generate_adversarial_examples(model)
    loss, acc = model.evaluate(x_test_adversarial, y_test)
    print(f"Model accuracy on adversarial examples: {acc * 100:.2f}%")

    # Plot a few adversarial examples
    num_examples = 5
    plt.figure(figsize=(10, 2))
    for i in range(num_examples):
        plt.subplot(1, num_examples, i + 1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(x_test_adversarial[i], cmap=plt.cm.binary)
        plt.xlabel(f"Label: {y_test[i]}")
    plt.show()

if __name__ == '__main__':
    load_and_evaluate_model()
