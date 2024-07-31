import numpy as np

# declaração da matriz A
A = np.array([[2., 4., 1.], [5., 2., 0.], [1., 1., 4.]])

# decomposição LU: A = L @ U
def decLU(A):

  n = A.shape[0]
  U = np.copy(A)
  L = np.identity(n)

  for j in range(n - 1):
    for i in range(j + 1, n):
      m = U[i, j]/U[j, j]
      U[i, j:] -= m * U[j, j:]
      L[i, j] = m

  return L, U

L, U = decLU(A)

print(L)
print(U)