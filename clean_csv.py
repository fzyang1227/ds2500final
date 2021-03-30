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

project_directory = 'C:\\Users\\fzyan\\Documents\\College\\ds2500project' # INSERT YOUR PROJECT DIRECTORY HERE
path = project_directory + '\\initial_data'

def clean_csv(df):
    return df

def open_csv():
    ''' Function: open_csv
        Parameters: none
        Returns: nothing
        Does: Takes Kickstarter files and modifies them to filter out specific columns
              and returns them as a toned down csv file in another subfolder
    '''
    if not os.path.exists('clean_data'):
        os.makedirs('clean_data')
    for filename in glob.glob(os.path.join(path, '*.csv')):
        df = pd.read_csv(filename)
        clean_df = clean_csv(df)
        if path in filename:
            csv_name = filename.replace(path, '')

        clean_df.to_csv(project_directory + '\\clean_data\\' + csv_name, index = False)










