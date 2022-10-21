import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pdb


e_df ='data/RM14_expdf.pickle'
e = pd.read_pickle(e_df)

kinematics ='data/kinematics_s3.csv'
predictions = 'data/predictions_s3.csv'
reachprocess_preds = 'data/reachprocess_preds_s3.txt'
prediction_val = pd.read_csv(predictions, index_col=False)
kinematics_val = pd.read_csv(kinematics, index_col=False)
reach_information = pd.read_csv(reachprocess_preds)


for idx, row in reach_information.iterrows():
    # Plot information for each index
    t_flag = False
    n_grasp = 0
    line_type = False
    if 'f' or 'F' in row['Type']:
        line_type = '*'
    start = row['Reach Start']
    stop = row['Reach Stop']
    n_grasp = row['Num Grasp']
    if 'r' or 'R' in row['Hand']:
        color_mark = 'b'
    if 'l' or 'L' in row['Hand']:
        color_mark = 'g'
    if 'bi' or 'Bi' in row['Hand']:
        color_mark = 'r'
    if 'Y' or 'y' in row['Tug of War']:
        t_flag = True
pdb.set_trace()

for idx, row in e.iterrows():
    if '0920' in row['Date']:
        if '3' in row['S']:
            start_times = row['r_start']
        if '1' in row['S']:
            start_times_s1 = row['r_start']




pdb.set_trace()