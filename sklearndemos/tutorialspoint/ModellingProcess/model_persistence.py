# https://www.tutorialspoint.com/scikit_learn/scikit_learn_modelling_process.htm
print('sklearndemos.tutorialspoint.ModellingProcess.model_persistence.py')

from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

iris = load_iris()

X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)
classifier_knn = KNeighborsClassifier(n_neighbors=3)
classifier_knn.fit(X_train, y_train)
y_pred = classifier_knn.predict(X_test)

pred_camp = zip(y_test, y_pred)
for pair in pred_camp:
    print(pair)



# Finding accuracy by comparing actual response values(y_test)with predicted response value(y_pred)
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
# Providing sample data and the model will make prediction out of that data

sample = [[5, 5, 3, 2], [2, 4, 3, 5]]
preds = classifier_knn.predict(sample)
pred_species = [iris.target_names[p] for p in preds]
print("Predictions:", pred_species)


import joblib
joblib.dump(classifier_knn, 'classifier_knn.joblib')

loaded_classifier_knn = joblib.load('classifier_knn.joblib')
new_preds = loaded_classifier_knn.predict(sample)
pred_species = [iris.target_names[p] for p in preds]
print("Predictions:", pred_species)

