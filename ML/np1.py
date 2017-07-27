import sys
import numpy

def arrays(arr):
    # Complete this function
    # a = arr
    arr.reverse()
    return numpy.array(arr, 'float64')

arr = map(float, raw_input().strip().split(' '))
result = arrays(arr)
print(result)
