import numpy as np

class NeuralNetwork:

    def __init__(self, n_layers, shapes):
        self.w_l = []
        for i in range(n_layers):
            self.w_l.append(2*np.random.random(shapes[i]) - 1)

    def train(self, data):
        
