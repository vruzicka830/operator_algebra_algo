import numpy as np

def direct_sum(A, B):
    """
    Compute the direct sum of two matrices, represent by block diagonal matrix.

    Args:
        A: A 2D numpy array (matrix) of shape (m, n)
        B: A 2D numpy array (matrix) of shape (p, q)

    Returns:
        A 2D numpy array of shape (m+p, n+q) containing A and B on the diagonal
    """
    # Input validation
    if not isinstance(A, np.ndarray) or not isinstance(B, np.ndarray):
        raise TypeError("Both inputs must be numpy arrays.")

    if A.ndim != 2 or B.ndim != 2:
        raise ValueError("Both inputs must be 2D arrays (matrices).")

    # Get dimensions
    A_rows, A_cols = A.shape
    B_rows, B_cols = B.shape

    # Use complex dtype to handle complex matrices (preserves real matrices too)
    result = np.zeros((A_rows + B_rows, A_cols + B_cols), dtype=complex)

    # Place A in the top-left block
    result[0:A_rows, 0:A_cols] = A

    # Place B in the bottom-right block
    result[A_rows:A_rows + B_rows, A_cols:A_cols + B_cols] = B

    return result

'''Example:
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
C = direct_sum(A,B)
s = direct_sum(A,B).shape
print(C,s)
'''
