# HowManyButtons.py
# Simple script to run when you want to check how many paths exist in the log file. Useful for checking progress.

import pandas as pd
import os


def get_num_paths(log_file_name):
    df = pd.read_csv(log_file_name, header=None)
    df.columns = ['button_id', 'action', 'x', 'y', 't', 'button_x', 'button_y', 'button_width', 'button_height']
    button_start_df = df.sort_values(by='t').groupby(['button_x',
                                                      'button_y',
                                                      'button_width',
                                                      'button_height']).first().reset_index()
    return len(button_start_df)


def main():

    log_file_name = input('Enter the name of the logging file you want to check: ')

    while not os.path.exists('data\\' + log_file_name):
        print('Could not find {} inside the data folder. Try again.'.format(log_file_name))
        log_file_name = input('Enter the name of the logging file you want to check: ')

    num_paths = get_num_paths('data\\' + log_file_name)

    print()
    print('Number of paths in {}: {}'.format(log_file_name, num_paths))


if __name__ == '__main__':
    main()
