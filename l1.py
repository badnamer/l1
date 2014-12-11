import numpy as np


# testing numpy
A=np.array([[1,2,3],[4,5,6],[7,8,9]],dtype='f')
I=np.eye(A.shape[0])
np.dot(A,I)
A[:,[x for x in range(3) if x != 1]]


# l1
def opt_l1(A, b, _lambda, epsilon=1e-7, maxit=100000):
	'''minimizes ||Ax-b||_2 + lambda*||x||_1'''
	# initial x
	d = A.shape[1]
	x = np.zeros(d)
	notConverged = True
	iteration = 0
	while notConverged:
		notConverged = True and (iteration<= maxit)
		currentOpt = np.linalg.norm(A.dot(x))**2+_lambda*np.linalg.norm(x,1)
		for i in range(d):
		# 2*A{i}'*((A{-i}*x{-i}+A{i}x{i}-b)) + delta|x{i}| = 0
			A_negI = A[:,[idx for idx in range(d) if idx!=i]]
			A_i = A[:,i]
			x_negI = x[[idx for idx in range(d) if idx!=i]]
			t = _lambda/A_i.dot(A_i)
			y = A_i.dot(b-A_negI.dot(x_negI))/A_i.dot(A_i)
			if y > t:
				x[i] = y-t
			elif y < -t:
				x[i] = y+t
			else:
				x[i] = 0
			newOpt = np.linalg.norm(A.dot(x))**2+_lambda*np.linalg.norm(x,1)
			currentOpt = newOpt
			if abs(newOpt-currentOpt) < epsilon:
				notConverged=False
		iteration += 1
		print x
		print np.linalg.norm(A.dot(x)-b,2)			
	return x
	



