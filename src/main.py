import numpy as np
from math import ceil
import matplotlib.pyplot as plt
import json
import pandas as pd
import seaborn as sns

from tensorflow import keras
from tensorflow.keras import models, layers
import time

def reconstruct_matrix(data):
    # Declaration of a three-dimensional numpy matrix with two channels (side 1 and side 2) to give to a CNN.
    # The matrix will be filled with the energy deposited in each sparse coordinate (same coordinates as in the matrix).
    # The first channel is filled with the energy from the hits of the side 1 and the second channel is filled with the energy from hits of the side 2.
    
    for event, event_data in data.items():
        gruid_hits_side_1 = event_data['gruid hits - side 1']
        gruid_hits_side_2 = event_data['gruid hits - side 2']
        gruid_metadata = event_data['gruid metadata']
     
    matrix = np.zeros((gruid_metadata['# of rows (y)'], gruid_metadata['# of columns (x)'], 2))

    # IMPORTANT: Coordinates are inverted in the matrix because of matrix notation in GRUID.
    
    # Side 1
    for timestamp, timestamp_data in gruid_hits_side_1.items():
        for pixel, pixel_data in timestamp_data.items():
            x, y = pixel.split(",")
            matrix[ int(y), int(x), 0 ] = pixel_data['energy deposited']

    # Side 2
    for timestamp, timestamp_data in gruid_hits_side_2.items():
        for pixel, pixel_data in timestamp_data.items():
            x, y = pixel.split(",")
            matrix[ int(y), int(x), 1 ] = pixel_data['energy deposited']
        
    return matrix


# Data loading
with open('../gruid-translator/out/out_bcal_2023-05-12T01:50:18_1-0.json') as f:
    data = json.load(f)    

matrix = reconstruct_matrix(data)


# CNN
# We will use a CNN to classify the events.
# The CNN will have two convolutional layers, two max pooling layers and two dense layers.
# The first convolutional layer will have 32 filters and the second convolutional layer will have 64 filters.
# The first dense layer will have 64 neurons and the second dense layer will have 2 neurons (one for each class).
# The activation function of the first dense layer will be ReLU and the activation function of the second dense layer will be softmax.
# The loss function will be categorical crossentropy and the optimizer will be Adam.
# The metrics will be accuracy, AUC and F1-score.

model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(matrix.shape[0], matrix.shape[1], 2)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(2, activation='softmax'))

model.compile(optimizer='adam',
                loss='categorical_crossentropy',
                metrics=['accuracy', keras.metrics.AUC(), keras.metrics.Precision(), keras.metrics.Recall(),
                         keras.metrics.FalsePositives(), keras.metrics.FalseNegatives(), keras.metrics.TruePositives(),
                         keras.metrics.TrueNegatives(), keras.metrics.PrecisionAtRecall(0.5), keras.metrics.RecallAtPrecision(0.5),
                         keras.metrics.AUC(curve='PR'), keras.metrics.AUC(curve='ROC'), keras.metrics.PrecisionAtRecall(0.5),
                         keras.metrics.RecallAtPrecision(0.5), keras.metrics.AUC(curve='PR'), keras.metrics.AUC(curve='ROC')]
                )

model.summary()
