from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
import random



#X = np.array([1,2,3,4,5,6], dtype=np.float64)
#Y = np.array([5,4,6,5,6,7], dtype=np.float64)

def createdata(n, var, stp=2, cor=False):
    val = 1
    Y = []
    for _ in range(n):
        y = val + random.randrange(-var, var)
        Y.append(y)
        if cor and cor == 'pos':
            val += stp
        elif cor and cor == 'neg':
            val -= stp
        X = [i for i in range(len(Y))]
    return np.array(X, dtype=np.float64), np.array(Y, dtype=np.float64)


def slope_intercept(X, Y):
    x_, y_ = mean(X), mean(Y)
    m = ((x_*y_ - mean(X*Y))/
         (x_**2 - mean(X**2)))
    c = mean(Y) - m*mean(X)
    return (m,c)


def sq_error(Y, y):
    return sum((y-Y)**2)


def r(Y, y):
    ymeanline = [mean(Y) for i in Y]
    sqerrorregr = sq_error (Y, y)
    sqerrormean = sq_error (Y, ymeanline)
    return 1 - (sqerrorregr/sqerrormean)


X, Y = createdata(40, 10, 2, 'pos')

    
z = slope_intercept(X, Y)
reg_line = [(z[0]*x)+z[1] for x in X]
r = r(Y, reg_line)
print r


plt.scatter(X, Y)
plt.plot(X, reg_line)
plt.show()
