import matplotlib.pyplot as plt
import numpy as np


data = {-1:np.array([[1,7],[2,8],[3,8]]),
         1:np.array([[5,1],[6,-1],[7,3]])}


class SupportVector(object):
    """docstring for SupportVector"""
    def __init__(self, visualize=True):
        self.visualize = visualize
        self.colours = {1:'r', -1:'b'}
        if self.visualize:
            self.fig = plt.figure()
            self.axis = self.fig.add_subplot(1, 1, 1)

    def fit(self, data):
        self.data = data
        opt_dict = {}  # {||w||: [w,b]}
        tfms = [[1, 1],
               [-1, 1],
               [-1, -1],
               [1, -1]]
        all_data = []
        for yi in self.data:
            for featuresset in self.data[yi]:
                for features in featuresset:
                    all_data.append(features)
        self.max_val = max(all_data)
        self.min_val = min(all_data)
        all_data = None
        stp_sizes = [self.max_val * 0.1,
                     self.max_val * 0.01,
                     self.max_val * 0.001]
        b_mult = 5
        b_mult_rng = 5
        latest_optimum = self.max_val * 10
        for stp in stp_sizes:
            w = np.array([latest_optimum, latest_optimum])
            optimised = False
            while not optimised:
                for b in np.arange(-1 * self.max_val * b_mult_rng,
                                   self.max_val * b_mult_rng,
                                   stp * b_mult):
                    for tfm in tfms:
                        w_t = w * tfm
                        found_options = True
                        for i in self.data:
                            for xi in self.data[i]:
                                yi = i
                                if not yi * (np.dot(w_t, xi) + b) >= 1:
                                    found_options = False
                                    break
                        if found_options:
                            opt_dict[np.linalg.norm(w_t)] = [w_t, b]
                if w[0] < 0:
                    optimised = True
                    print "optimised a step"
                else:
                    w = w - stp
            norms = sorted([n for n in opt_dict])
            opt_choice = opt_dict[norms[0]]
            self.w = opt_choice[0]
            self.b = opt_choice[1]
            latest_optimum = opt_choice[0][0] + stp*2

    def predict(self, features):
        # sign (x.w + b)
        clf = np.sign(np.dot(np.array(features), self.w) + self.b)
        if clf and self.visualize:
            self.axis.scatter(features[0], features[1], s=200, marker=*, c=self.colours[clf])
        return clf

    def visulaize(self):
        self.axis.scatter(features[0], features[1], s=200, marker=*, c=self.colours[clf])