import sys
import math
import csv
import os
import argparse
from column import *
import numpy as np
import pandas as pd
import json
import matplotlib.pyplot as plt

class Train:
    def __init__(self, data, iterations, lr, visu):
        data['t0'] = np.ones(data.loc[:, 'Hogwarts House'].shape[0])
        self.selected_features = ["Hogwarts House",'t0', "Herbology", "Ancient Runes", "Astronomy", "Charms", "Defense Against the Dark Arts"]
        self.data = data.loc[:, self.selected_features]
        self.lr = lr
        self.visu = visu
        self.iterations = iterations
        self.predictions = {}
        self.costs = {}
        self.houses = self.data.loc[:, "Hogwarts House"].unique()

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def train(self):
        std_deviations, means, x = self.ft_standardize(self.data.loc[:, self.selected_features[2:]])
        x.insert(0, "t0", self.data.loc[:, 't0'])
        self.predictions['standard'] = {'std': list(std_deviations), 'mean': list(means)}
        self.predictions['houses'] = {}
        m = x.shape[0]
        for house in self.houses:
            cost = []
            thetas = np.zeros((x.shape[1]))
            y = self.is_from_house(house)
            for i in range(self.iterations):
                z = np.dot(x, thetas)
                h = self.sigmoid(z)
                j = (1 / m) * (np.dot(-y.T, np.log(h)) - np.dot((1 - y).T, np.log(1 - h)))
                cost.append(j)
                gradient = np.dot(x.T, (h - y)) / y.size
                thetas -= self.lr * gradient
            self.predictions['houses'][house] = list(thetas)
            self.costs[house] = list(cost)
        if self.visu:
            for house in self.houses:
                plt.plot(self.costs[house])
            plt.show()
        with open('data.json', 'w+') as json_file:  
            json.dump(self.predictions,  json_file)

    def is_from_house(self, house):
        return np.where(self.data.loc[:, self.selected_features[0]] == house, 1, 0)

    def ft_standardize(self, matrix):
        return [matrix.std(), matrix.mean(), ((matrix - matrix.mean()) / matrix.std())]


args = argparse.ArgumentParser("Statistic description of your data file")
args.add_argument("file", help="File to descripte", type=str)
args.add_argument("-i", "--iter", help="The number of iterations to go through the regression", default=10000, type=int)
args.add_argument("-l", "--learning", help="The learning rate to use during the regression", default=0.01, type=float)
args.add_argument("-v", "--visu", help="Visualize functions", action="store_true", default=False)
args = args.parse_args()

if os.path.isfile(args.file):
    try:
        df = pd.read_csv(args.file, sep=',')
        df = df.dropna()
        Train(df, args.iter, args.learning, args.visu).train()
        
    except Exception as e:
        raise(e)
        sys.stderr.write(str(e) + '\n')
        sys.exit()
else:
    sys.stderr.write("Invalid input\n")
    sys.exit(1)