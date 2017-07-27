from math import sqrt
from collections import Counter
import numpy as np
import pandas as pd
import random
import warnings



def KNN(data, predict, k=3, radius=-1):
    d = []
    if len(data) >= k:
        warnings.warn('K is set to a value less than total voting groups')
    if radius == -1:
        for group in data:
            for features in data[group]:
                eu_dist = np.linalg.norm(np.array(features)-np.array(predict))
                d.append([eu_dist, group])
        votes = [i[1] for i in sorted(d)[:k]]
        result = Counter(votes).most_common(1)[0][0]
    return result

#test data
df = pd.read_csv('breast-cancer-wisconsin.data')
df.replace('?', -99999, inplace=True)
df.drop(['id'], 1, inplace=True)
full_data = df.astype(float).value.tolist()
random.shuffle(full_data)
test_size = 0.2
train_set = {2:[], 4:[]}
test_set = {2:[], 4:[]}
train_data = fulldata[:-int(test_size*len(full_data))]
test_data = fulldata[-int(test_size*len(full_data)):]

[train_set[i[-1]].append(i[:-1]) for i in train_data]

result = KNN(data, new)
print result
