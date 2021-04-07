'''
    DS2500 project
    clean_csv
    takes the Kickstarter csv files and cleans them
    return a csv
    utilizes pandas dataframe
'''
import time
import csv
import os
import glob
import pandas as pd
import re
import string
import json
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def map_location_pledged_data():
    from urllib.request import urlopen
    import json
    with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
        counties = json.load(response)

    import pandas as pd
    df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
                       dtype={"fips": str})

    import plotly.express as px

    fig = px.choropleth(df, geojson=counties, locations='fips', color='unemp',
                               color_continuous_scale="Viridis",
                               range_color=(0, 12),
                               scope="usa",
                               labels={'unemp':'unemployment rate'}
                              )
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.show()

def get_location_pledged_data():
    ''' Function: get_location_pledged_data
        Parameters: none
        Returns: Map of cities to amount of money pledged
        Does: Goes through each cleaned csv and calculates a running total
        of pledged data per city
    '''

    data = {}

    path = 'clean_data'
    for filename in glob.glob(os.path.join(path, '*.csv')):
        print(filename)
        df = pd.read_csv(filename)
        # print(df)
        for index, row in df.iterrows():
            if row['location'] not in data:
                data[row['location']] = 0
            data[row['location']] += row['pledged']
    # data = sorted(data.items(), key=lambda item: item[1])
    # print(data)
    graph_pledged_data(data, 'Amount of Dollars Raised in City', 'Dollars Raised', 'Dollars')

def graph_pledged_data(dataRaw, title, values1Label, ylabel):
    dataRawSorted = sorted(dataRaw.items(), key=lambda item: item[1])
    data = dataRawSorted[len(dataRawSorted)-10:]

    # creating the dataset
    keys = []
    values1 = []
    for city in data:
        keys.append(city[0])
        values1.append(round(city[1], 2))
    # courses = list(data.keys())
    # values = list(data.values())

    x = np.arange(len(keys))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, values1, width, label=values1Label)

    # Add some text for keys, title and custom x-axis tick keys, etc.
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.set_xticks(x)
    ax.set_xticklabels(keys)
    ax.legend()

    autolabel(rects1, ax)

    fig.tight_layout()

    plt.show()


def get_location_success_failure_data():
    ''' Function: get_location_success_failure_data
        Parameters: none
        Returns: Map of cities to how many success and failed
        Does: Goes through each cleaned csv and calculates the total successful
        and failed kickstarters
    '''

    data = {}

    path = 'clean_data'
    for filename in glob.glob(os.path.join(path, '*.csv')):
        print(filename)
        df = pd.read_csv(filename)
        # print(df)
        for index, row in df.iterrows():
            if row['location'] not in data:
                data[row['location']] = {'successful': 0, 'failed': 0}
            if row['state'] == 'successful':
                data[row['location']]['successful'] += 1
            if row['state'] == 'failed':
                data[row['location']]['failed'] += 1
    for cityName in data:
        city = data[cityName]
        total = city['successful'] + city['failed']
        if total < 50:
            city['successfulRate'] = 0
            city['failedRate'] = 0
            continue
        successfulRate = city['successful'] / total
        failedRate = city['failed'] / total
        city['successfulRate'] = successfulRate
        city['failedRate'] = failedRate
    # data = sorted(data.items(), key=lambda item: item[1]['successfulRate'])
    # print(data)
    graph_success_failure_data(data, 'successful', 'failed', 'Cities with most Successes', 'Succeeded', 'Failed', 'Number of Startups')
    # graph_success_failure_data(data, 'failed', 'successful', 'Cities with most Failed', 'Succeeded', 'Failed', 'Number of Startups')
    graph_success_failure_data(data, 'successfulRate', 'failedRate', 'Cities highest success and failure rate', 'Successful Rate', 'Failed Rate', 'Percent of startups')
    # graph_success_failure_data(data, 'successfulRate')
    # graph_success_failure_data(data, 'failedRate')
    # graph_success_failure_data(data, 'failed')


def graph_success_failure_data(dataRaw, key1, key2, title, values1Label, values2Label, ylabel):
    dataRawSorted = sorted(dataRaw.items(), key=lambda item: item[1][key1])
    data = dataRawSorted[len(dataRawSorted)-10:]

    # creating the dataset
    keys = []
    values1 = []
    values2 = []
    for city in data:
        keys.append(city[0])
        values1.append(round(city[1][key1], 2))
        values2.append(round(city[1][key2], 2))
    # courses = list(data.keys())
    # values = list(data.values())

    x = np.arange(len(keys))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, values1, width, label=values1Label)
    rects2 = ax.bar(x + width/2, values2, width, label=values2Label)

    # Add some text for keys, title and custom x-axis tick keys, etc.
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.set_xticks(x)
    ax.set_xticklabels(keys)
    ax.legend()

    autolabel(rects1, ax)
    autolabel(rects2, ax)

    fig.tight_layout()

    plt.show()


def autolabel(rects, ax): # This function was taken from https://matplotlib.org/stable/gallery/lines_bars_and_markers/barchart.html#sphx-glr-gallery-lines-bars-and-markers-barchart-py
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')
