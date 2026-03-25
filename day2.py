import numpy as np

def direct_sum(A,B):

	A_rows, A_cols = A.shape
	B_rows, B_cols = B.shape

	sum = np.zeros((A_rows+B_rows,A_cols+B_cols))

	sum[0:A_rows, 0:A_cols] = A
	sum[A_rows:A_rows+B_rows, A_cols:A_cols+B_cols] = B

	return sum
