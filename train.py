import pandas as pd
import numpy as np
from neuralnetwork import ImitationLearning
import tensorflow as tf
from sklearn.model_selection import train_test_split

y = pd.read_csv("y_tree.csv")
print(y.shape)

X = np.load("X_tree.npy")
print(X.shape)

x_train, x_val, y_train, y_val = train_test_split(X, y)

model = ImitationLearning(64, y.shape[1])
model.compile(optimizer='adam',
              loss=tf.keras.losses.CategoricalCrossentropy(),
              metrics=['accuracy'])

model.neurons.load_weights('./checkpoints/my_checkpoint')

"""history = model.neurons.fit(x_train, y_train, epochs=1,
                            validation_data=(x_val, y_val))

model.neurons.save_weights('./checkpoints/my_checkpoint')"""

idx = 16

output = model.neurons.predict(tf.expand_dims(x_val[idx], axis=0))[0]

print(output)
print(y_val.iloc[idx])
print(np.argmax(output))
print(y_val.iloc[idx].argmax())
