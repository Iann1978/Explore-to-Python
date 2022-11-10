# https://www.tutorialspoint.com/scikit_learn/scikit_learn_modelling_process.htm
print('sklearndemos.tutorialspoint.ModellingProcess.train_test_split.py')

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

print("Shape of X_train:", X_train.shape)
print("Shape of y_train", y_train.shape)
print("Shape of X_test", X_test.shape)
print("Shape of y_test:", y_test.shape)
