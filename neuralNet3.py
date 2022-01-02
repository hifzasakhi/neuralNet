import sys
import numpy as np
import matplotlib


inputs = [1, 2, 3, 2.5]

weights1 = [0.2, 0.8, -0.5, 1.0]
weights2 = [0.5, -0.91, 0.26, -0.50]
weights3 = [-0.26, -0.27, 0.17, 0.87]
bias1 = 2
bias2 = 3
bias3 = 0.5

weights = [weights1, weights2, weights3]
biases = [bias1, bias2, bias3]

#dot product doesnt matter which one you supply first, same answer which is scalar
#however, whatever parameter passed in first is what determines the indexing here
output = np.dot(weights, inputs) + biases

print ("output: " + str(output))