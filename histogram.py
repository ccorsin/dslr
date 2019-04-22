import sys
import math
import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class Analysis:
    def __init__(self, data):
        self.data = data
        self.index = len(data[0])
        self.titles = self.get_titles()

    def ft_max_count(self):
        i = 0
        for row in self.data:
            i += 1
        return float(i)

    def analyze(self):
        self.columns = []
        self.count = self.ft_max_count()
        i = 0
        j = 0
        while i < len(self.data[0]):
            j = 0
            col = []
            while j < self.count:
                try:
                    float(self.data[0][i])
                    col.append(float(self.data[j][i]))
                    j += 1
                except:
                    j += 1
            self.columns.append(col)
            i += 1
        self.houses = self.get_houses()
        self.print_graph()

    def print_graph(self):
        i = 1
        k = 1
        std = []
        labels = []
        while i < len(self.columns):
            if len(self.columns[i]):
                house1 = self.get_from_house(self.houses[0], self.columns[i])
                # house2 = self.get_from_house(self.houses[1], self.columns[i])
                # house3 = self.get_from_house(self.houses[2], self.columns[i])
                # house4 = self.get_from_house(self.houses[3], self.columns[i])
                plt.subplot(7, 2, k)
                plt.title(self.titles[i])
                plt.xlabel('Grades')
                plt.ylabel('Frequencies')
                # plt.hist([house1, house2, house3, house4], range = (-25000, 11000))
                k += 1
            i += 1
        plt.subplots_adjust(hspace = 1)
        # plt.show()

    def get_titles(self):
        with open('dataset_train.csv') as f:
            reader = csv.reader(f, delimiter=',')
            d = list(reader)
            return d[0]

    def get_houses(self):
        houses = []
        i = 0
        while i < self.count:
            if self.data[i][1] not in houses:
                houses.append(self.data[i][1])
            i += 1
        return houses

    def get_from_house(self, name, col):
        l = []
        i = 0
        while i < len(col):
            if self.columns[1][i] == name:
                l.append(col[i])
            i += 1
        return l

try:
    # df = pd.read_csv('dataset_train.csv', sep=',',header=None)
    # df = df.iloc[1:]
    # df = df.astype(dtype= {7:"float64"})
    # print (df[7].describe())
    with open('dataset_train.csv') as f:
        reader = csv.reader(f, delimiter=',')
        next(reader)
        d = list(reader)
    Analysis(d).analyze()
except Exception as e:
    sys.stderr.write(str(e) + '\n')
    sys.exit()