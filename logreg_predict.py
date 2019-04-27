import json
import argparse
import sys
import os
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
    args = args.parse_args()
    if os.path.isfile(args.file):
        try:
            df = pd.read_csv(args.file, sep=',')
            df = df.dropna()
            json_file = open('data.json')
            data_json = json.load(json_file)
            theta_dic = data_json['houses']
        except Exception as e:
            sys.stderr.write("Le fichier n'est pas correct\n")
            sys.exit(1)
    else:
        sys.stderr.write("Le fichier n'est pas correct\n")
        sys.exit(1)
    # df['t0'] = np.ones(df.loc[:, 'Hogwarts House'].shape[0])
    df_part = ft_standardize(df.loc[: , ["Herbology", "Ancient Runes", "Astronomy", "Charms", "Defense Against the Dark Arts"]], data_json['standard']['mean'], data_json['standard']['std'])
    df_part.insert(0, 't0', np.ones(df.loc[:, 'Hogwarts House'].shape[0]))
    predictions = []
    true_result = []
    for index, row in df_part.iterrows():
        predictions.append(prediction(theta_dic, row))
        true_result.append(df.loc[index, 'Hogwarts House'])
    print(accuracy_score(true_result, predictions))
        # with open('results.csv', 'w+') as csvfile:
        #     fieldnames = ['theta0', 'theta1']
        #     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        #     writer.writeheader()
        #     writer.writerow({'theta0': self.theta0, 'theta1': self.theta1})
    
    
    