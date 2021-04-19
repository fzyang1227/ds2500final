'''
    DS 2500 Project
    Driver code
'''
from clean_csv import *
from map_data import *
from blurb_data import *


if __name__ == '__main__':
    # open_csv()
    csv = read_csv()
    word_dict = blurb(csv)
    visualize_blurb(word_dict)
    get_location_success_failure_data()
    get_location_pledged_data()