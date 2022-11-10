# https://www.tutorialspoint.com/scikit_learn/scikit_learn_modelling_process.htm
print('sklearndemos.tutorialspoint.ModellingProcess.mean_removal.py')

import numpy as np
from sklearn import preprocessing

Input_data = np.array(
    [[2.1, -1.9, 5.5],
    [-1.5, 2.4, 3.5],
    [0.5, -7.9, 5.6],
    [5.9, 2.3, -5.8]]
)

# Displaying the mean and the standard deviation of the input data
print ('Mean of input data:', Input_data.mean(axis=0))
print ('Standard deviation of input data:', Input_data.std(axis=0))

# Removing the mean and
data_scaled = preprocessing.scale(Input_data)
print('Mean_removed =', data_scaled.mean(axis=0))
print('Stddeviation_removed =', data_scaled.std(axis=0))
print('data_input:', Input_data)
print('data_removed:', data_scaled)
