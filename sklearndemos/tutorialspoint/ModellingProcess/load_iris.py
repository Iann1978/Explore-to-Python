# https://www.tutorialspoint.com/scikit_learn/scikit_learn_modelling_process.htm
print('sklearndemos.tutorialspoint.ModellingProcess.load_iris.py')

from sklearn.datasets import load_iris

iris = load_iris()
X = iris.data
Y = iris.target
print("Shape of data:",  iris.data.shape)
print("Shape of target:",  iris.target.shape)
print("Feature names:", iris.feature_names)
print("Target names:", iris.target_names)
print("\nFirst 10 rows of data:\n", iris.data[:10])