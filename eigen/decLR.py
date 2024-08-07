import numpy as np

# declaração da matriz A
A = np.array([[2., 4., 1.], [5., 2., 0.], [1., 1., 4.]])

# máximas iterações
maxIter = 100

# decomposição LR
def decLR(A):

  n = A.shape[0]
  R = np.copy(A)
  L = np.identity(n)

  for j in range(n - 1):
    for i in range(j + 1, n):
      m = R[i, j]/R[j, j]
      R[i, j:] -= m * R[j, j:]
      L[i, j] = m

  return L, R

L, R = decLR(A)

print(L)
print(R)