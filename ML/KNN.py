from sklearn import preprocessing, model_selection, neighbors
import numpy as np
import pandas as pd



df = pd.read_csv('breast-cancer-wisconsin.data')
df.replace('?', -99999, inplace=True)
df.drop(['id'], 1, inplace=True)

y = np.array(df['class'])
X = np.array(df.drop(['class'], 1))

X_train, X_test, y_train, y_test = model_selection.train_test_split(X,y,test_size=0.2)

clf = neighbors.KNeighborsClassifier()
clf.fit(X_train, y_train)

acc = clf.score(X_test, y_test)
print "%f" %(acc*100)

#test data for K Nearest Neighbours
test = np.array([[4,2,1,1,1,2,3,2,1],[4,2,1,2,1,2,3,2,1]])
pr = clf.predict(test.reshape(len(test), -1))
print pr
