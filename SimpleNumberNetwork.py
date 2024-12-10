import tensorflow as tf
import numpy as np
from tensorflow import keras

# Create the Neural Network (1 Layer Deep, 1 Neuron, 1 Input)
model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])

# Define the Loss and Optimizer for the Network 
#   Optimizer = sgd (stochastic gradient descent)
#   Loss = mean_squared_error
model.compile(optimizer='sgd', loss='mean_squared_error')

# Define Data for Network
xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-2.0, 1.0, 4.0, 7.0, 10.0, 13.0], dtype=float)

# Provide the Network with Data
model.fit(xs, ys, epochs=500)

print(model.predict(np.array([10.0])))
