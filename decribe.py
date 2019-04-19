import pandas as pd
import sys
import math
import csv
import numpy as np

class Analysis:
    def __init__(self, data):
        self.data = data
        # self.index = len(data[0])
        self.index = 15

    def ft_count(self):
        i = 0
        for row in self.data:
            i += 1
        return float(i)

    def ft_mean(self, j):
        sum = 0
        i = 0
        k = 0
        while i < self.count:
            try:
                sum += float(self.data[i][j])
                i += 1
                k += 1
            except:
                i+= 1
        return float(sum / k)

    def ft_std(self, j):
        sum = 0
        i = 0
        k = 0
        mean = self.ft_mean(j)
        while i < self.count:
            try:
                sum += (float(self.data[i][j]) - mean) * (float(self.data[i][j]) - mean)
                i += 1
                k += 1
            except:
                i += 1
        return math.sqrt((1 / (k - 1) * sum)) 

    def ft_min(self, j):
        mini = float(self.data[0][j])
        i = 0
        while i < self.count:
            try:
                if float(self.data[i][j]) < mini:
                    mini = float(self.data[i][j])
                i += 1
            except:
                i += 1
        return mini

    def ft_max(self, j):
        maxi = float(self.data[0][j])
        i = 0
        while i < self.count:
            try:
                if float(self.data[i][j]) > maxi:
                    maxi = float(self.data[i][j])
                i += 1
            except:
                i += 1
        return maxi

    def ft_percentile(self, j, percentile):

        mini = self.ft_min(j)
        maxi = self.ft_max(j)
        return math.ceil(mini + (maxi - mini) * percentile)


    def analyze(self):
        self.columns = []
        self.count = self.ft_count()
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
            print (len(self.columns[i]))
            i += 1
        # self.print_line(' ')
        # self.print_line('Count')
        # self.print_line('Mean')
        # self.print_line('Std')
        # self.print_line('Min')
        # self.print_line('25%')
        # self.print_line('50%')
        # self.print_line('75%')
        # self.print_line('Max')

    def print_line(self, string):
        i = 0
        line_new = '{:>12}  '.format(string)
        while i < self.index:
            if len(self.columns[i]):
                if string == ' ':
                    line_new += '{:>12}  '.format('Feature' + str(i + 1))
                elif string == 'Count':
                    line_new += '{:>12.6f}  '.format(self.ft_count())
                elif string == 'Mean':
                    line_new += '{:>12.6f}  '.format(self.ft_mean(i))
                elif string == 'Std':
                    line_new += '{:>12.6f}  '.format(self.ft_std(i))
                elif string == 'Min':
                    line_new += '{:>12.6f}  '.format(self.ft_min(i))
                elif string == 'Max':
                    line_new += '{:>12.6f}  '.format(self.ft_max(i))
                elif string == '25%':
                    line_new += '{:>12.6f}  '.format(self.ft_percentile(i, 0.25))
                elif string == '50%':
                    line_new += '{:>12.6f}  '.format(self.ft_percentile(i, 0.5))
                elif string == '75%':
                    line_new += '{:>12.6f}  '.format(self.ft_percentile(i, 0.75))
                i += 1
        print (line_new)

try:
    # df = pd.read_csv('dataset_train.csv', sep=',',header=None)
    # df = df.iloc[1:]
    # df = df.astype(dtype= {11:"float64"})
    # print (df[11].describe())
    with open('dataset_train.csv') as f:
        reader = csv.reader(f, delimiter=',')
        next(reader)
        d = list(reader)
    Analysis(d).analyze()
except Exception as e:
    sys.stderr.write(str(e) + '\n')
    sys.exit()