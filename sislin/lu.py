import numpy as np


def LU_decomposition(A):
    """Perform LU decomposition of a square matrix (numpy array) using the Doolittle factorization."""
    
    L = np.zeros_like(A, dtype=float)
    U = np.zeros_like(A, dtype=float)
    N = np.size(A, 0)

    for k in range(N):
        L[k, k] = 1
        U[k, k] = A[k, k] - np.dot(L[k, :k], U[:k, k]) 
        for j in range(k+1, N):
            U[k, j] = A[k, j] - np.dot(L[k, :k], U[:k, j])
        for i in range(k+1, N):
            L[i, k] = (A[i, k] - np.dot(L[i, :k], U[:k, k])) / U[k, k]

    return L, U

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) # creates an A matrix

b = np.array([9, 8, 3]) # creates a b vector

L, U = LU_decomposition(A) # decomposes A into L and U matrices

m = len(A) # the number of rows of A

x = np.zeros(b.size) # creates an x matrix
y = np.zeros(b.size) # creates a y matrix

print(L);
print(U);
print(L@U);