import numpy as np

def nonlin(x, deriv=False):
	if deriv:
		return (x*(1-x))

	return 1/(1+np.exp(-x))

# test input data
x = np.array([[0,0,1],
			  [0,1,1],
			  [1,0,1],
			  [1,1,1]])

y = np.array([[0],
			 [1],
			 [1],
			 [0]])

np.random.seed(1)

w_l0 = 2*np.random.random((3,4)) - 1
w_l1 = 2*np.random.random((4,1)) - 1

#train
for i in range(300000):
	l0 = x
	l1 = nonlin(np.dot(l0, w_l0))
	l2 = nonlin(np.dot(l1, w_l1))
	
	l2_error = y - l2
	l2_del = l2_error*nonlin(l2, deriv=True)
	l1_error = l2_del.dot(w_l1.T)
	l1_del = l1_error*nonlin(l1, deriv=True)
	
	w_l1 += l1.T.dot(l2_del)
	w_l0 += l0.T.dot(l1_del)

error_matrix = y - l2

print("output after training")
print(l1)
print("accuracy:")
print(1 - np.mean(np.abs(error_matrix)))
