# PP4 for CS 107 pair programming
# Group members: Max Li. Gabin Ryu, Aleksander Aleksiev
# Coder: Max Li
# Listener: Gabin Ryu
# Sharer: Aleksander Aleksiev

import numpy as np

def layer(shape, actv): 
    def innerFn(inputs, weight, bias):
        # check that inputs / weights / bias match the shape
        if np.shape(weight)[0] != shape[0] or np.shape(weight)[1] != shape[1]:
            raise ValueError("Weights array is incorrect shape; expected " + str(shape[0]) + " by " + str(shape[1]))
        if np.shape(bias)[1] != shape[1]:
            raise ValueError("Bias array is incorrect shape; expected " + str(shape[1]))
        if np.shape(inputs)[1] != shape[0]:
            raise ValueError("Input array is incorrect shape; expected " + str(shape[0]))

        output = actv(np.dot(inputs, weight) + bias)
        return output
    return innerFn

t = np.random.uniform(0.0, 1.0, 2).reshape(1,-1) # input to the network

# Initialise shapes
shape1 = [1,2]
shape2 = [2,4]

layer1 = layer(shape1, np.tanh) # Define layer 1
layer2 = layer(shape2, np.tanh) # Define layer 2

# Initialize weights and biases
w1 = np.array([[1,2]])
w2 = np.array([[1,2,4,2],[3,2,1,2]])
b1 = np.array([[5,6]])
b2 = np.array([[5,6,7,8]])

# Run through the network
h1 = layer1(t, w1, b1) # First layer
h2 = layer2(h1, w2, b2) # Last layer

print(t)
print(h1)
print(h2)