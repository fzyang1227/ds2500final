"""
Wesley Chung
DS2500 Final
Spring 2021
"""

import pandas as pd
from dectree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from blurb_data import blurb

def read_csv_short():
    df = pd.read_csv('clean_data\\Kickstarter.csv') 
    df = df[["backers_count", "goal", "pledged", "state"]]
    df.loc[df['state'] == 'canceled', 'state'] = 0
    df.loc[df['state'] == 'failed', 'state'] = 0
    df.loc[df['state'] == 'live', 'state'] = 1
    df.loc[df['state'] == 'successful', 'state'] = 1
    
    return df

def dectree(depth):
    dataset = read_csv_short()
    training_set = dataset.copy()   
    training_target = training_set[["state"]]    
    training_features = training_set.drop(["state"], axis = 1)
    
    training_features = training_features.to_numpy()    
    training_target = training_target.to_numpy().reshape(1, -1)[0]    
    clf = DecisionTreeClassifier(max_depth = depth) 
    clf.fit(training_features, training_target)
    predicted = clf.predict(dataset.to_numpy())
    correct = 0
    total = 0
    for i in range(len(dataset)):    
        actual = dataset.iloc[i]['state']
        if predicted[i] == actual:
            correct += 1
        total += 1
    
    return correct/total

if __name__ == '__main__':
    x = []
    y = []
    for i in range(8):
        x.append(i)
        y.append(dectree(i))
    
    plt.plot(x, y)
    plt.show()
    