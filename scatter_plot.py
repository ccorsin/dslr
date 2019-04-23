import sys
import math
import csv
from column_adjusted import *
import matplotlib.pyplot as plt
import numpy as np

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
        err = []
        i = 0
        while i < len(self.data[0]):
            self.clean_data[i] = Column(self.data, i, self.count, self.titles, err)
            i += 1
        i = 0
        self.ft_remove_columns(self.clean_data, err)
        self.print_graph()

    def print_graph(self):
        i = 1
        std = []
        labels = []
        while i < len(self.clean_data) - 1:
            if self.clean_data[i].type == 'Num':
                j = i + 1
                fig = plt.figure(i, figsize=(15, 10))
                fig.suptitle(self.titles[i])
                k = 1
                while j < len(self.clean_data):
                    if self.clean_data[j].type == 'Num':
                        plt.subplot(7, 2, k)
                        plt.scatter(self.clean_data[i].data, self.clean_data[j].data, alpha=0.5)
                        plt.xlabel(self.titles[i])
                        plt.ylabel(self.titles[j])
                    j += 1
                    k += 1
                plt.subplots_adjust(hspace = 1)
            i += 1
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

    def ft_remove_columns(self, data, errors):
        i = 0
        errors.sort(reverse=True)
        while i < len(data):
            for el in errors:
                del data[i].data[el]
            data[i].len = len(data[i].data)
            i += 1

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