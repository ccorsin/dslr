import json
import argparse
import sys
import os
import pandas as pd
import numpy as np

def prediction(thetas, data):
    house = None
    score = None
    for key, value in thetas.items():
        tmp = np.dot(thetas[key], data)
        if (score is None or tmp > score):
            score = tmp
            house = key
    return house
        

if __name__ == '__main__':
    args = argparse.ArgumentParser("Predict houses from data")
    args.add_argument("file", help="File to descripte", type=str)
    args = args.parse_args()
    result = []
    if os.path.isfile(args.file):
        try:
            df = pd.read_csv(args.file, sep=',')
            df = df.dropna()
            json_file = open('data.json')
            theta_dic = json.load(json_file)
        except Exception as e:
            sys.stderr.write("Le fichier n'est pas correct\n")
            sys.exit(1)
    else:
        sys.stderr.write("Le fichier n'est pas correct\n")
        sys.exit(1)
    df['t0'] = np.ones(df.loc[:, 'Hogwarts House'].shape[0])
    df = df.loc[: , ['t0', "Herbology", "Ancient Runes", "Astronomy", "Charms", "Defense Against the Dark Arts"]]
    for index, row in df.iterrows():
        result.append(prediction(theta_dic, row))
        with open('results.csv', 'w+') as csvfile:
            fieldnames = ['theta0', 'theta1']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'theta0': self.theta0, 'theta1': self.theta1})
    
    
    