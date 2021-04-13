'''
    DS2500 project
    blurb_analysis
    reads column, success/fail
    counts most successful words, least successful words
'''

import pandas as pd
import json
import matplotlib.pyplot as plt

STOPWORDS =["a", "an", "and", "the", "to", "i", "if", "of", "that", "it",
            "is", "im", "has", "was", "his", "ive", "at", "in", "your", "its",
            "for", "this", "are", "as", "be", "not", "have", "but", "with",
            "by", "no", "dont", 'on', 'from', 'our', 'about']

def read_csv():
    
    df = pd.read_csv('clean_data\\Kickstarter.csv')
    csv_list = df.values.tolist()
        
    return csv_list

def blurb(csv):
    words = {}
    for row in csv:
        blurb = row[1].split()
        for i in range(len(blurb)):
            if blurb[i] in STOPWORDS:
                continue
            if blurb[i] not in words:
                words[blurb[i]] = 0
            if row[15] == 'successful':
                words[blurb[i]] += 1
            if row[15] == 'failed':
                words[blurb[i]] -= 1
    
    sorted_words = dict(sorted(words.items(), key=lambda item: item[1], reverse=True))          
    
    return list(sorted_words.items())[:20]

def visualize_blurb(word_dict):
    x_list = []
    y_list = []
    for i in range(len(word_dict)):
        x_list.append(word_dict[i][0])
        y_list.append(word_dict[i][1])
    plt.bar(x_list, y_list)
    plt.title('Frequency of Words by Success/Failure, Top 20')
    plt.xlabel('Word')
    plt.xticks(rotation = 90)
    plt.ylabel('Frequency')
    for i in range(len(x_list)):
        plt.annotate(str(y_list[i]), xy=(x_list[i],y_list[i]), ha='center', va='bottom')
    plt.show()

    