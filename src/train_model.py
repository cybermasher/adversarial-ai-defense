# src/train_model.py

import tensorflow as tf
import optuna
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense, Dropout
from tensorflow.keras.optimizers import Adam, RMSprop
from functools import lru_cache

@lru_cache(maxsize=1)
def load_mnist_data():
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
    x_train, x_test = x_train / 255.0, x_test / 255.0
    return (x_train, y_train), (x_test, y_test)

def build_model(trial):
    model = Sequential()
    model.add(Flatten(input_shape=(28, 28)))
    model.add(Dense(trial.suggest_int('units', 32, 512), activation='relu'))
    model.add(Dropout(trial.suggest_float('dropout', 0.2, 0.5)))
    model.add(Dense(10, activation='softmax'))

    optimizer_options = {'adam': Adam, 'rmsprop': RMSprop}
    optimizer_name = trial.suggest_categorical('optimizer', ['adam', 'rmsprop'])
    optimizer = optimizer_options[optimizer_name]()

    model.compile(optimizer=optimizer, loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model

def objective(trial):
    (x_train, y_train), (x_test, y_test) = load_mnist_data()

    model = build_model(trial)

    history = model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=5, batch_size=32, verbose=0)

    accuracy = history.history['val_accuracy'][-1]
    return accuracy

def train_with_optuna():
    study = optuna.create_study(direction='maximize')
    study.optimize(objective, n_trials=50)

    print('Number of finished trials:', len(study.trials))
    print('Best trial:')
    trial = study.best_trial

    print('  Value:', trial.value)
    print('  Params:')
    for key, value in trial.params.items():
        print('    {}: {}'.format(key, value))

    best_model = build_model(trial)
    (x_train, y_train), (x_test, y_test) = load_mnist_data()
    best_model.fit(x_train, y_train, epochs=5, verbose=1)
    best_model.save('models/mnist_model_optuna.h5')

if __name__ == '__main__':
    train_with_optuna()
