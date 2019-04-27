import sys
import math
import csv
import os
import argparse
from column import *
import numpy as np
import pandas as pd

class Analysis:
    def __init__(self, data):
        self.data = data
        self.index = len(data[0])
        self.titles = self.get_titles()

    def get_titles(self):
        with open('dataset_train.csv') as f:
            reader = csv.reader(f, delimiter=',')
            d = list(reader)
            return d[0]

    def ft_count(self, i):
        return float(self.clean_data[i].len)

    def ft_max_count(self):
        i = 0
        for row in self.data:
            i += 1
        return float(i)

    def ft_mean(self, j):
        sum = 0
        i = 0
        while i < self.clean_data[j].len:
            sum +=  self.clean_data[j].data[i]
            i += 1
        return float(sum / self.clean_data[j].len)

    def ft_std(self, j):
        sum = 0
        i = 0
        mean = self.ft_mean(j)
        while i < self.clean_data[j].len:
            sum += (self.clean_data[j].data[i] - mean) * (self.clean_data[j].data[i] - mean)
            i += 1
        return math.sqrt((1 / (self.clean_data[j].len - 1) * sum)) 

    def ft_min(self, j):
        mini = self.clean_data[j].data[0]
        i = 0
        while i < self.clean_data[j].len:
            if self.clean_data[j].data[i] < mini:
                mini = self.clean_data[j].data[i]
            i += 1 
        return mini

    def ft_max(self, j):
        maxi = self.clean_data[j].data[0]
        i = 0
        while i < self.clean_data[j].len:
            if self.clean_data[j].data[i] > maxi:
                maxi = self.clean_data[j].data[i]
            i += 1
        return maxi

    def ft_percentile(self, sorted_list, percentile):
        position = (len(sorted_list) - 1) * (percentile)
        f = math.floor(position)
        c = math.ceil(position)
        if f == c:
            return sorted_list[int(position)]
        d0 = sorted_list[int(f)] * (c - position)
        d1 = sorted_list[int(c)] * (position - f)
        return d0 + d1


    def analyze(self):
        self.clean_data = {}
        self.count = self.ft_max_count()
        i = 0
        j = 0
        while i < len(self.data[0]):
            self.clean_data[i] = Column(self.data, i, self.count, self.titles)
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
            if self.clean_data[i].type == 'Num':
                self.clean_data[i].data.sort()
                if string == ' ':
                    line_new += '{:>14}  '.format('Feature' + str(i + 1))
                elif string == 'Count':
                    line_new += '{:>14.6f}  '.format(self.ft_count(i))
                elif string == 'Mean':
                    line_new += '{:>14.6f}  '.format(self.ft_mean(i))
                elif string == 'Std':
                    line_new += '{:>14.6f}  '.format(self.ft_std(i))
                elif string == 'Min':
                    line_new += '{:>14.6f}  '.format(self.ft_min(i))
                elif string == 'Max':
                    line_new += '{:>14.6f}  '.format(self.ft_max(i))
                elif string == '25%':
                    line_new += '{:>14.6f}  '.format(self.ft_percentile(self.clean_data[i].data, 0.25))
                elif string == '50%':
                    line_new += '{:>14.6f}  '.format(self.ft_percentile(self.clean_data[i].data, 0.5))
                elif string == '75%':
                    line_new += '{:>14.6f}  '.format(self.ft_percentile(self.clean_data[i].data, 0.75))
            i += 1
        print (line_new)

args = argparse.ArgumentParser("Statistic description of your data file")
args.add_argument("file", help="File to descripte", type=str)
args = args.parse_args()

if os.path.isfile(args.file):
    try:
        df = pd.read_csv('dataset_train.csv', sep=',',header=None)
        df = df.iloc[1:]
        df = df.astype(dtype= {0:"float64"})
        value = pd.Series(df[0])
        print (value.describe())
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