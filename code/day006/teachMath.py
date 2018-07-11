# From Sololearn, Android App
# Teaching a computer to predict the output of a mathematical expression without
# "knowing" the exact formula, using neural networks and back propagation
# one single neuron with two inputs and one outputs
# The actual expression is (a+b)*2

from numpy import exp, array, random, dot

class neural_network:
    def __init__(self):
        random.seed(1)
        self.weights = 2 * random.random((2, 1)) - 1

    def train(self, inputs, outputs, num):
        for iteration in range(num):
            output = self.think(inputs)
            error = outputs - output
            adjustment = 0.01*dot(inputs.T, error)
            self.weights += adjustment

    def think(self, inputs):
        return (dot(inputs, self.weights))

neural_network = neural_network()

#Our training set
inputs = array([[2, 3], [1, 1], [5, 2], [12, 3]])
outputs = array([[10, 4, 14, 30]]).T

#Training the neural network with the training set
neural_network.train(inputs, outputs, 10000)

#Show us the output
print(neural_network.think(array[15, 2]))
