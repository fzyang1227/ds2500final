"""
Wesley Chung
DS2500 Final
Spring 2021
"""

import pandas as pd
import graphviz
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn import tree
import matplotlib.pyplot as plt

def read_csv_short():
    df = pd.read_csv('clean_data\\Kickstarter.csv') 
    df = df[["backers_count", "goal", "pledged", "spotlight", "staff_pick", "preview_time", "fundraising_time", "state"]]
    df['state'] = df['state'].map({'canceled': 0, 'failed': 1, 'live': 2, 'successful': 3})
    df['spotlight'] = df['spotlight'].map({False: 0, True: 1})
    df['staff_pick'] = df['staff_pick'].map({False: 0, True: 1})
    
    return df

def dectree(depth, dataset):
    df = dataset.copy()   
    y = df["state"]  
    X = df.drop(["state"], axis = 1)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
    clf = tree.DecisionTreeClassifier(max_depth=depth) 
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    
    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred, output_dict = True))
    
    dot_data = tree.export_graphviz(clf, out_file=None, feature_names=X.columns)
    
    graph = graphviz.Source(dot_data, format="png")
    graph.render("decision_tree_graphivz")
    
    accuracy = classification_report(y_test, y_pred, output_dict=True)['accuracy'] 
    precision = classification_report(y_test, y_pred, output_dict=True)['weighted avg']['precision']
    recall = classification_report(y_test, y_pred, output_dict=True)['weighted avg']['recall']
    f1 = classification_report(y_test, y_pred, output_dict=True)['weighted avg']['f1-score']
    
    return (accuracy, precision, recall, f1)
    
def dectreeplot(depth, dataset):
    x = []
    y1 = []
    y2 = []
    y3 = []
    y4 = []
    for i in range(1, depth):
        x.append(i)
        y1.append(dectree(i, dataset)[0])
        y2.append(dectree(i, dataset)[1])
        y3.append(dectree(i, dataset)[2])
        y4.append(dectree(i, dataset)[3])
    
    plt.plot(x, y1)
    plt.xlabel("Max Depth")
    plt.ylabel("Accuracy")
    plt.title("Decision Tree Max Depth and Accuracy")
    plt.xticks(np.arange(0, len(x)+1, 2))
    plt.show()
    
    plt.plot(x, y2)
    plt.xlabel("Max Depth")
    plt.ylabel("Precision")
    plt.title("Decision Tree Max Depth and Precision")
    plt.xticks(np.arange(0, len(x)+1, 2))
    plt.show()
    
    plt.plot(x, y3)
    plt.xlabel("Max Depth")
    plt.ylabel("Recall")
    plt.title("Decision Tree Max Depth and Recall")
    plt.xticks(np.arange(0, len(x)+1, 2))
    plt.show()
    
    plt.plot(x, y4)
    plt.xlabel("Max Depth")
    plt.ylabel("f1-Score")
    plt.title("Decision Tree Max Depth and f1-Score")
    plt.xticks(np.arange(0, len(x)+1, 2))
    plt.show()
