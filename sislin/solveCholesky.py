import numpy as np

# declaração da matriz A e do vetor coluna b
A = np.array([[1, 2, 3, 4], [2, 20, 18, 16], [3, 18, 19, 21], [4, 16, 21, 33]])
b = np.array([4, 6, 8, 8])

# decomposição de cholesky: A = L @ L^T
def cholesky(A):
    L = A.copy()
    n = A.shape[0]

    for k in range(n):
        try:
            L[k,k] = np.sqrt(L[k, k]- L[k, 0:k]@L[k, 0:k])
        except ValueError:
            print('Matriz não é definida e positiva')
        for i in range(k + 1, n):
            L[i, k] = (L[i, k] - L[i, 0:k]@L[k, 0:k])/L[k, k]

    for k in range(1, n): 
        L[0:k, k] = 0.0

    return L

def solveCholesky(A, b):

  n = b.size
  x = np.zeros((n))
  y = np.zeros((n))
  L = cholesky(A)

  for k in range(n):
    y[k] = (b[k] - L[k, 0:k]@y[0:k])/L[k, k]

  for k in range(n - 1, -1, -1):
     x[k] = (y[k] - L[k + 1:n, k]@x[k + 1:n])/L[k, k]

  return x

x = solveCholesky(A, b)

print(x)