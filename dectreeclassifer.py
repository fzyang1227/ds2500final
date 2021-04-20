"""
Wesley Chung
DS2500 Final
Spring 2021
"""

import pandas as pd
import graphviz
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn import tree
import matplotlib.pyplot as py 

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
    print(classification_report(y_test, y_pred))
    
    dot_data = tree.export_graphviz(clf, out_file=None, feature_names=X.columns)
    
    graph = graphviz.Source(dot_data, format="png")
    graph.render("decision_tree_graphivz")
    
    return classification_report(y_test, y_pred, output_dict=True)['accuracy'] 
    
def dectreeplot(depth, dataset):
    x = []
    y = []
    for i in range(1, depth):
        x.append(i)
        y.append(dectree(i, dataset))
    py.plot(x, y)
    py.xlabel("Max Depth")
    py.ylabel("Accuracy")
    py.title("Decision Tree Max Depth and Accuracy")
