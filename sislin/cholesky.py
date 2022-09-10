import numpy as np;

# declaração da matriz A
A = np.array([[1, 2, 3, 4], [2, 20, 18, 16], [3, 18, 19, 21], [4, 16, 21, 33]]);

# decomposição de cholesky: A = L @ L^T
def cholesky(A):
    L = A.copy();
    n = A.shape[0];

    for k in range(n):
        try:
            L[k,k] = np.sqrt(L[k, k]- L[k, 0:k]@L[k, 0:k]);
        except ValueError:
            print('Matriz não é definida e positiva');
        for i in range(k + 1, n):
            L[i, k] = (L[i, k] - L[i, 0:k]@L[k, 0:k])/L[k, k];

    for k in range(1, n): 
        L[0:k, k] = 0.0;

    return L;

L = cholesky(A);

print(L);