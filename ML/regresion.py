import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
from matplotlib import style
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression
import quandl
import math

style.use('ggplot')
df = quandl.get('WIKI/GOOGL')
#print df.head

df = df[["Adj. Open","Adj. High","Adj. Low","Adj. Close","Adj. Volume"]]
df["%High-Low"] = (df["Adj. High"] - df["Adj. Low"]) * 100 / df["Adj. Low"]
df["%Change"] = (df["Adj. Close"] - df["Adj. Open"]) * 100 / df["Adj. Open"]
df = df[["Adj. Close","%High-Low","%Change","Adj. Volume"]]
#print df.head

forecast = "Adj. Close"
df.fillna(-99999, inplace=True)

out = int(math.ceil(0.01*len(df)))
df['prediction'] = df[forecast].shift(-out)
#print df.head()

X = np.array(df.drop(['prediction'],1))
X = preprocessing.scale(X)
X_lately = X[-out:] 
X = X[:-out]

df.dropna(inplace=True)
y = np.array(df['prediction'])
y = np.array(df['prediction'])
#print len(X),len(y)

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)
clf = LinearRegression(n_jobs=-1)
clf.fit(X_train, y_train)
accuracy = clf.score(X_test, y_test)
#print accuracy*100

forecast_set = clf.predict(X_lately)
print (forecast_set, accuracy, out)
df['Forecast'] = np.nan
last_date = df.iloc[-1].name
last_unix = time.mktime(last_date.timetuple())﻿
one_day = 86400
next_unix = last_unix + one_day

for i in forecast_set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += one_day
    df.loc[next_date] = [np.nam for a in range(len(df.columns)-1)] + [i]

df['Adj. Close'].plot()
df['Forecast'].plot()
plt.legend(loc=4)
plt.xlable('Date')
plt.ylable('Price')
plt.show()
