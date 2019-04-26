import sys
import math
import csv
from column_adjusted import *
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

try:
    df = pd.read_csv('dataset_train.csv', sep=',')
    sns.set(style="ticks", color_codes=True)
    df.pop('Index')
    sns.pairplot(df.dropna(), hue = "Hogwarts House")
    plt.tight_layout()
    plt.savefig('pair_plot.pdf')
except Exception as e:
    sys.stderr.write(str(e) + '\n')
    sys.exit()