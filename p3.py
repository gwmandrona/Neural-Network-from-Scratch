# Cleaner and more dynamic way of calculating the output of 3 neurons in a layer
inputs = [1, 2, 3, 2.5]

# A matrix of vectors
weights = [[0.2, 0.8, -0.5, 1.0],
           [0.5, -0.91, 0.26, -0.5],
           [-0.26, -0.27, 0.17, 0.87]]

biases = [2, 3, 0.5]


some_value = 0.5
weight = -0.7
bias = 0.7

# Meant to show two different tools that can change the output using either the weight or the bias
print(some_value*weight)
print(some_value+bias)






'''
# Making a loop that mutliplies the weights and inputs together, and then adds the biases at the end
layer_outputs = [] # Output of the current layer
for neuron_weights, neuron_bias in zip(weights, biases): # Zip combines two lists into a list of lists, kind of element wise
    neuron_output = 0  # Output of given neuron
    for n_input, weight in zip(inputs, neuron_weights):
        neuron_output += n_input*weight
    neuron_output += neuron_bias
    layer_outputs.append(neuron_output)

print(layer_outputs)
'''