import numpy as np


# testing numpy
A=np.array([[1,2,3],[4,5,6],[7,8,9]],dtype='f')
I=np.eye(A.shape[0])
np.dot(A,I)
A[:,[x for x in range(3) if x != 1]]


# l1
def opt_l1(A, b, _lambda, epsilon):
	'''minimizes ||Ax-b||_2 + lambda*||x||_1'''
	# initial x
	d = A.shape[0]
	x = np.zeros(d)
	converged = False
	while norm(A.dot(x)-b) > epsilon:
		for i in range(d):
		# 2*A{i}'*((A{-i}*x{-i}+A{i}x{i}-y)) + delta|x{i}| = 0
			A_negI = A[:,[idx for idx in range(d) if idx!=i]]
			A_i = A[:,i]
			x_negI = x[[idx for idx in range(d) if idx!=i]]
			t = lambda_/A_i.dot(A_i)
			y = A_i.dot(y-A_negI.dot(x_negI))/A_i.dot(A_i)
			if y > t:
				x_i = y-t
			elif y < t:
				x_i = y+t
			else:
				x_i = 0			
	return x
	



