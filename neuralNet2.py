import sys
import numpy as np
import matplotlib

#print ("Python: ", sys.version)
#print ("Numpy: ", np.version)
#print ("Matplotlib: ", matplotlib.__version__)

#3 output neurons, each of which have the same 3 inputs coming in at diff weight
#each output neuron has its own bias 
inputs = [1, 2, 3, 2.5]
weights1 = [0.2, 0.8, -0.5, 1.0]
weights2 = [0.5, -0.91, 0.26, -0.50]
weights3 = [-0.26, -0.27, 0.17, 0.87]
bias1 = 2
bias2 = 3
bias3 = 0.5

weights = [weights1, weights2, weights3]
biases = [bias1, bias2, bias3]

layer_outputs = [] #Output of current layer
#zip fxn combines 2 lists elment wise
for neurons_weights, neuron_bias in zip(weights, biases): 
	neuron_output = 0 #output of given neuron 
	for n-input, weight in zip (inputs, neurons_weights):
		neuron_output += n_input * weight 
	neuron_output += neuron_bias
	layer_outputs.append(neuron_output)

print ("layer_outputs: " + str(layer_outputs))