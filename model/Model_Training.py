import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Input
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.utils import to_categorical

# Cargar el conjunto de datos CIFAR-10
(X_train, y_train), (X_test, y_test) = cifar10.load_data()
# Imprimir tamaño del conjunto de entrenamiento
print(f"Train Size: {len(X_train)} \n Size: {len(X_train[0])}x{len(X_train[0][0])} \n {X_train[0]}")

# Normalizar los datos
X_train = X_train.astype('float32') / 255
X_test = X_test.astype('float32') / 255
# Imprimir tamaño del conjunto de entrenamiento y la primera imagen
print(f"Train Size: {len(X_train)} \n {len(X_train[0])} \n {X_train[0]}")

# Codificar las etiquetas
y_train = to_categorical(y_train, num_classes=10)
y_test = to_categorical(y_test, num_classes=10)
# Imprimir tamaño de las etiquetas de entrenamiento y un ejemplo
print(f"Size Train Labels: {len(y_train)} \n {y_train[2]}")

# CIFAR-10 tiene imágenes de 32x32
# CIFAR-10 tiene 10 clases

data = models.Sequential([
    layers.Conv2D(96, (3, 3), strides=(1, 1), activation='relu', input_shape=(32, 32, 3)),
    layers.MaxPooling2D(pool_size=(2, 2), strides=(2, 2)),
    layers.Conv2D(256, (3, 3), activation='relu', padding='same'),
    layers.MaxPooling2D(pool_size=(2, 2), strides=(2, 2)),
    layers.Conv2D(384, (3, 3), activation='relu', padding='same'),
    layers.Conv2D(384, (3, 3), activation='relu', padding='same'),
    layers.Conv2D(256, (3, 3), activation='relu', padding='same'),
    layers.MaxPooling2D(pool_size=(2, 2), strides=(2, 2)),
    layers.Flatten(),
    layers.Dense(4096, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(4096, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(10, activation='softmax'),
])

data.summary()

# Compilar el modelo
data.compile(optimizer=Adam(), loss='categorical_crossentropy', metrics=['accuracy'])

# Entrenar el modelo
data.fit(X_train, y_train, epochs=20, batch_size=128, validation_data=(X_test, y_test))

# Guardar el modelo entrenado
data.save('proyecto_deep.h5')  # Guardar el modelo en un archivo .h5