import numpy as np

def direct_sum(A,B):

	A_rows, A_cols = A.shape
	B_rows, B_cols = B.shape

	sum = np.zeros((A_rows+B_rows,A_cols+B_cols), dtype=complex)

	sum[0:A_rows, 0:A_cols] = A
	sum[A_rows:A_rows+B_rows, A_cols:A_cols+B_cols] = B

	return sum

A = np.array([[1+1j, 2],[3,4-2j]], dtype = complex)
B = np.array([[-3+5j, -2],[3+2j,1-1j]], dtype = complex)

print("Direct sum of A and B: ")
print(direct_sum(A,B))

print("Tensor product of A and B: ")
print(np.kron(A,B))
