# Working with a dot product example for three neurons

import numpy as np

inputs = [1, 2, 3, 2.5]
weights = [[0.2, 0.8, -0.5, 1.0],
           [0.5, -0.91, 0.26, -0.5],
           [-0.26, -0.27, 0.17, 0.87]]

bias = [2, 3, 0.5]

# Notice that we pass the weights as the first variable, in order to index the function based on that
# This is because the number of neurons is dependant on the set of weights
output = np.dot(weights, inputs) + bias
print(output)

# Think of the weights * inputs + bias as a y=mx+b equation, and how changing the weight and bias can affect it