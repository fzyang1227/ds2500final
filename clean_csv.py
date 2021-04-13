'''
    DS2500 project
    clean_csv
    takes the Kickstarter csv files and cleans them
    return a csv
    utilizes pandas dataframe
'''
import csv
import os
import glob
import pandas as pd
import time
import re
import json

pd.options.mode.chained_assignment = None

project_directory = 'C:\\Users\\fzyan\\Documents\\College\\ds2500project' # INSERT YOUR PROJECT DIRECTORY HERE
path = project_directory + '\\initial_data'

data_col = ['backers_count', 'blurb', 'category', 'country_displayable_name',
            'created_at', 'creator', 'deadline', 'goal', 'id', 'launched_at',
            'location', 'name', 'pledged', 'slug', 'spotlight', 'staff_pick',
            'state', 'state_changed_at', 'urls', 'usd_pledged']

dict_col = ['category', 'location', 'urls']

def word_list(df):
    ''' Function: word_list
        Parameters: df (dataframe)
        Returns: df (dataframe)
        Does: changes the dataframe values of strings and cleans them
              into a list of lowercase words/numbers
    '''
    df = df[df['blurb'].apply(lambda x: isinstance(x, (str, bytes)))]
    df['blurb'] = [re.sub(r'[^ \nA-Za-z0-9/]+', '', x).lower() for x in df['blurb']]
    df['slug'] = [x.replace('-', ' ') for x in df['slug']]
    return df


def convert_val(df):
    ''' Function: convert_val
        Parameters: df (dataframe)
        Returns: df (dataframe)
        Does: changes the dataframe values of string dictionaries
              to actual values and gets needed values
    '''
    df['creator'] = [re.search('\"name\":\"(.+?)\",\"slug\"', x).group(1) if '\"slug\"' in x
                     else re.search('\"name\":\"(.+?)\",\"is_registered\"', x).group(1) for x in df['creator']]
    for col in dict_col:
        df = df[df[col].apply(lambda x: isinstance(x, (str, bytes)))]
        df[col] = [json.loads(x) for x in df[col]]
    df['category'] = [x['name'] for x in df['category']]
    df['location'] = [x['short_name'] for x in df['location']]
    df['urls'] = [x['web']['project'] for x in df['urls']]
    return df


def clean_csv(df_name):
    ''' Function: clean_csv
        Parameters: df_name (string of csv name)
        Returns: clean_df (dataframe)
        Does: cleans the data in the csv file through a dataframe
              removes specific columns and filters only US Kickstarters

    '''
    df = pd.read_csv(df_name, index_col = 'id', usecols = data_col)
    us_df = df[df.country_displayable_name == 'the United States']
    us_df = convert_val(us_df)
    us_df = word_list(us_df)
    return us_df


def open_csv():
    ''' Function: open_csv
        Parameters: none
        Returns: nothing
        Does: Takes Kickstarter files and modifies them to filter out specific columns
              and returns them as a toned down csv file in another subdirectory (clean_data)
    '''
    # creates clean_data folder
    if not os.path.exists('clean_data'):
        os.makedirs('clean_data')

    # gets names of files in initial_data folder
    start = time.time()
    for filename in glob.glob(os.path.join(path, '*.csv')):
        clean_df = clean_csv(filename)

        # removes path from filename for cleaner file names in clean_data folder
        if path in filename:
            csv_name = filename.replace(path, '')

        clean_df.to_csv(project_directory + '\\clean_data\\' + csv_name, index = False)
    end = time.time()
    print(end - start, 'seconds')
