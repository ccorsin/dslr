import sys
import math
import csv
import os
import argparse
import numpy as np
import pandas as pd

class Analysis:
    def __init__(self, data):
        self.data = data
        self.index = len(data[0])

    def ft_count(self, i):
        return float(len(self.columns[i]))

    def ft_max_count(self):
        i = 0
        for row in self.data:
            i += 1
        return float(i)

    def ft_mean(self, j):
        sum = 0
        i = 0
        while i < len(self.columns[j]):
            sum += self.columns[j][i]
            i += 1
        return float(sum / len(self.columns[j]))

    def ft_std(self, j):
        sum = 0
        i = 0
        mean = self.ft_mean(j)
        while i < len(self.columns[j]):
            sum += (float(self.columns[j][i]) - mean) * (float(self.columns[j][i]) - mean)
            i += 1
        return math.sqrt((1 / (len(self.columns[j]) - 1) * sum)) 

    def ft_min(self, j):
        mini = self.columns[j][0]
        i = 0
        while i < len(self.columns[j]):
            if self.columns[j][i] < mini:
                mini = self.columns[j][i]
            i += 1 
        return mini

    def ft_max(self, j):
        maxi = self.columns[j][0]
        i = 0
        while i < len(self.columns[j]):
            if self.columns[j][i] > maxi:
                maxi = self.columns[j][i]
            i += 1
        return maxi

    def ft_percentile(self, sorted_list, percentile):
        position = len(sorted_list) * (percentile)
        mini = sorted_list[math.floor(position)]
        maxi = sorted_list[math.ceil(position)]
        return mini + (maxi - mini) * (1 - percentile)


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
        self.print_line(' ')
        self.print_line('Count')
        self.print_line('Mean')
        self.print_line('Std')
        self.print_line('Min')
        self.print_line('25%')
        self.print_line('50%')
        self.print_line('75%')
        self.print_line('Max')

    def print_line(self, string):
        i = 0
        line_new = '{:>12}  '.format(string)
        while i < self.index:
            if len(self.columns[i]):
                self.columns[i].sort()
                if string == ' ':
                    line_new += '{:>12}  '.format('Feature' + str(i + 1))
                elif string == 'Count':
                    line_new += '{:>12.6f}  '.format(self.ft_count(i))
                elif string == 'Mean':
                    line_new += '{:>12.6f}  '.format(self.ft_mean(i))
                elif string == 'Std':
                    line_new += '{:>12.6f}  '.format(self.ft_std(i))
                elif string == 'Min':
                    line_new += '{:>12.6f}  '.format(self.ft_min(i))
                elif string == 'Max':
                    line_new += '{:>12.6f}  '.format(self.ft_max(i))
                elif string == '25%':
                    line_new += '{:>12.6f}  '.format(self.ft_percentile(self.columns[i], 0.25))
                elif string == '50%':
                    line_new += '{:>12.6f}  '.format(self.ft_percentile(self.columns[i], 0.5))
                elif string == '75%':
                    line_new += '{:>12.6f}  '.format(self.ft_percentile(self.columns[i], 0.75))
            i += 1
        print (line_new)

args = argparse.ArgumentParser("Statistic description of your data file")
args.add_argument("file", help="File to descripte", type=str)
args = args.parse_args()

if os.path.isfile(args.file):
    try:
        # df = pd.read_csv('dataset_train.csv', sep=',',header=None)
        # df = df.iloc[1:]
        # df = df.astype(dtype= {7:"float64"})
        # print (df[7].describe())
        with open(args.file) as f:
            reader = csv.reader(f, delimiter=',')
            next(reader)
            d = list(reader)
        Analysis(d).analyze()
    except Exception as e:
        sys.stderr.write(str(e) + '\n')
        sys.exit()
else:
    sys.stderr.write("Invalid input\n")
    sys.exit(1)