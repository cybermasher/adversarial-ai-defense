# src/defense_mechanism.py

import tensorflow as tf
from functools import lru_cache
from adversarial_attack import create_adversarial_pattern

@lru_cache(maxsize=1)
def load_mnist_data():
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
    x_train, x_test = x_train / 255.0, x_test / 255.0
    return (x_train, y_train), (x_test, y_test)

def adversarial_training():
    (x_train, y_train), (x_test, y_test) = load_mnist_data()
    model = tf.keras.models.load_model('models/mnist_model.h5')

    perturbations = create_adversarial_pattern(model, x_train, y_train)
    epsilon = 0.1
    x_train_adversarial = x_train + epsilon * perturbations

    x_train_combined = tf.concat([x_train, x_train_adversarial], axis=0)
    y_train_combined = tf.concat([y_train, y_train], axis=0)

    model.fit(x_train_combined, y_train_combined, epochs=5)
    model.save('models/adversarial_trained_model.h5')

if __name__ == '__main__':
    adversarial_training()
