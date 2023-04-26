import os
import tensorflow as tf


class ImitationLearning():
    def __init__(self, input_size, output_size):
        self.neurons = tf.keras.models.Sequential()
        self.neurons.add(tf.keras.layers.Rescaling(1./255, input_shape=(64, 64, 3)))
        self.neurons.add(tf.keras.layers.Conv2D(input_size, (3, 3), activation='relu'))
        self.neurons.add(tf.keras.layers.MaxPooling2D((2, 2)))
        self.neurons.add(tf.keras.layers.Conv2D(input_size*2, (3, 3), activation='relu'))
        self.neurons.add(tf.keras.layers.MaxPooling2D((2, 2)))
        self.neurons.add(tf.keras.layers.Conv2D(input_size*2, (3, 3), activation='relu'))
        self.neurons.add(tf.keras.layers.GlobalAveragePooling2D())
        self.neurons.add(tf.keras.layers.Dense(input_size*2, activation='relu'))
        self.neurons.add(tf.keras.layers.Dropout(.5))
        self.neurons.add(tf.keras.layers.Dense(input_size, activation='softmax'))
        self.neurons.add(tf.keras.layers.Dense(output_size, activation='softmax'))

    def compile(self,**kwargs):
        return self.neurons.compile(**kwargs)