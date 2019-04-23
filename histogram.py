import sys
import math
import csv
from column import *
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
        self.clean_data = {}
        self.count = self.ft_max_count()
        i = 0
        while i < len(self.data[0]):
            self.clean_data[i] = Column(self.data, i, self.count, self.titles)
            i += 1
        self.houses = self.get_houses()
        self.print_graph()

    def print_graph(self):
        i = 1
        k = 1
        std = []
        labels = []
        while i < len(self.clean_data):
            if self.clean_data[i].type == 'Num':
                house1 = self.get_from_house(self.houses[0], self.clean_data[i])
                house2 = self.get_from_house(self.houses[1], self.clean_data[i])
                house3 = self.get_from_house(self.houses[2], self.clean_data[i])
                house4 = self.get_from_house(self.houses[3], self.clean_data[i])
                plt.subplot(7, 2, k)
                plt.title(self.titles[i])
                plt.xlabel('Grades')
                plt.ylabel('Frequencies')
                plt.axvline(np.mean(house1), color='b', linestyle='dashed', linewidth=2)
                plt.axvline(np.mean(house2), color='#F1C40F', linestyle='dashed', linewidth=2)
                plt.axvline(np.mean(house3), color='g', linestyle='dashed', linewidth=2)
                plt.axvline(np.mean(house4), color='r', linestyle='dashed', linewidth=2)
                plt.axvline(np.mean(self.clean_data[i].data), color='k', linestyle='dashed', linewidth=2)
                plt.hist([house1, house2, house3, house4], normed=True)
                k += 1
            i += 1
        plt.subplots_adjust(hspace = 1)
        plt.show()

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
        while i < col.len:
            if self.clean_data[1].data[i] == name:
                l.append(col.data[i])
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