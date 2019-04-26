import sys
import math
import csv
import os
import argparse
from column import *
import numpy as np
import pandas as pd
import json

class Train:
    def __init__(self, data, iterations, lr):
        data['t0'] = np.ones(data.loc[:, 'Hogwarts House'].shape[0])
        self.selected_features = ["Hogwarts House",'t0', "Herbology", "Ancient Runes", "Astronomy", "Charms", "Defense Against the Dark Arts"]
        self.data = data.loc[:, self.selected_features]
        self.lr = lr
        self.iterations = iterations
        self.predictions = {}
        self.houses = self.data.loc[:, "Hogwarts House"].unique()
        # print(self.data.loc[:, "Hogwarts House"].unique())
        

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def train(self):
        x = self.data.loc[:, self.selected_features[1:]]
        for house in self.houses:
            thetas = np.zeros((x.shape[1]))
            y = self.is_from_house(house)
            for i in range(self.iterations):                 
                z = np.dot(x, thetas)
                # print(z.shape)
                h = self.sigmoid(z)
                gradient = np.dot(x.T, (h - y)) / y.size
                thetas -= self.lr * gradient
                # print (h)
            self.predictions[house] = list(thetas)
        with open('data.json', 'w+') as json_file:  
            json.dump(self.predictions, json_file)

    def is_from_house(self, house):
        return np.where(self.data.loc[:, self.selected_features[0]] == house, 1, 0)




args = argparse.ArgumentParser("Statistic description of your data file")
args.add_argument("file", help="File to descripte", type=str)
args.add_argument("-i", "--iter", help="The number of iterations to go through the regression", default=10000, type=int)
args.add_argument("-l", "--learning", help="The learning rate to use during the regression", default=0.01, type=float)
args = args.parse_args()

if os.path.isfile(args.file):
    try:
        df = pd.read_csv(args.file, sep=',')
        df = df.dropna()
        print(df)
        Train(df, args.iter, args.learning).train()
        
    except Exception as e:
        raise(e)
        sys.stderr.write(str(e) + '\n')
        sys.exit()
else:
    sys.stderr.write("Invalid input\n")
    sys.exit(1)