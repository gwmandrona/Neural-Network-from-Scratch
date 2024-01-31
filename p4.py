import numpy as np

# Batching the inputs, no need to change the weights or the biases because they just about remain the same
inputs = [[1, 2, 3, 2.5],
          [2.0, 5.0, -1.0, 2.0],
          [-1.5, 2.7, 3.3, -0.8]]

weights = [[0.2, 0.8, -0.5, 1.0],
           [0.5, -0.91, 0.26, -0.5],
           [-0.26, -0.27, 0.17, 0.87]]

biases = [2, 3, 0.5]

# Start of the second layer in the neural network
weights2 = [[0.1, -0.14, 0.5],
           [-0.5, 0.12, -0.33],
           [-0.44, 0.73, -0.13]]

biases2 = [-1, 2, -0.5]

layer1_outputs = np.dot(inputs, np.array(weights).T) + biases

layer2_outputs = np.dot(layer1_outputs, np.array(weights2).T) + biases2

print(layer2_outputs)


'''
output = np.dot(inputs, weights) + biases
print(output)

This does not work because the inputs would be trying to multiply themselves by the first index for each list in the weights, but when
they get to the fourth index of the inputs, there is no 4th list within the weights. So to fix this we need to transpose the matrixes
'''


# the greater of batches that we have, the easier it would be for the neuron to fit to the general idea / equation of the data