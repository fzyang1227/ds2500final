'''
    DS 2500 Project
    Driver code
'''
from clean_csv import *
from map_data import *
from blurb_data import *
from dectreeclassifer import *


if __name__ == '__main__':
    # open_csv()
    csv = read_csv()
    word_dict = blurb(csv)
    visualize_blurb(word_dict)
    get_location_success_failure_data()
    get_location_pledged_data()
    
    dataset = read_csv_short()
    
    # plots max depth until 20
    dectreeplot(20, dataset)
    
    # highest accuracy, recall, f1-score png saved at max_depth = 3
    dectree(3, dataset)
    
    # highest precision png saved at max_depth = 6
    # will overwrite last png, use saved pngs
    dectree(6, dataset)