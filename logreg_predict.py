import json
import argparse
import sys
import os
import csv
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score

def prediction(thetas, data):
    house = None
    score = None
    for key, value in thetas.items():
        tmp = np.dot(thetas[key], data)
        if (score is None or tmp > score):
            score = tmp
            house = key
    return house

def ft_standardize(matrix, mean, std):
    return (matrix - mean) / std

if __name__ == '__main__':
    args = argparse.ArgumentParser("Predict houses from data")
    args.add_argument("file", help="File to descripte", type=str)
    args.add_argument("thetas", help="Trained parameters", type=str)
    args = args.parse_args()
    if os.path.isfile(args.file):
        try:
            df = pd.read_csv(args.file, sep=',')
            if os.path.isfile(args.thetas):
                try:
                    json_file = open(args.thetas)
                    data_json = json.load(json_file)
                    theta_dic = data_json['houses']
                except Exception as e:
                    sys.stderr.write("Le fichier n'est pas correct\n")
                    sys.exit(1)
            else:
                sys.stderr.write("Le fichier n'est pas correct\n")
                sys.exit(1)
        except Exception as e:
            sys.stderr.write("Le fichier n'est pas correct\n")
            sys.exit(1)
    else:
        sys.stderr.write("Le fichier n'est pas correct\n")
        sys.exit(1)
    df_part = df.loc[: , ["Astronomy", "Herbology", "Ancient Runes", "Charms"]]
    df_part.fillna(df_part.median(), inplace=True)
    df_part = ft_standardize(df_part.loc[: , ["Astronomy", "Herbology", "Ancient Runes", "Charms"]], data_json['standard']['mean'], data_json['standard']['std'])
    df_part.insert(0, 't0', np.ones(df_part.shape[0]))
    predictions = []
    true_result = []
    with open('houses.csv', 'w+') as csvfile:
        fieldnames = ['Index', 'Hogwarts House']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for index, row in df_part.iterrows():
            predictions.append(prediction(theta_dic, row))
            true_result.append(df.loc[index, 'Hogwarts House'])
            writer.writerow({'Index': index, 'Hogwarts House': prediction(theta_dic, row)})
    
    
    