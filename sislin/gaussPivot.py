import numpy as np

# declaração da matriz A e do vetor coluna b
A = np.array([[2., 4., 1.], [5., 2., 0.], [1., 1., 4.]])
b = np.array([1., 0., 0.])

# substituição sucessiva (matrizes triangulares superiores)
def substRet(U, b):

  n = b.size
  x = np.zeros(n)

  for i in reversed(range(n)):
    x[i] = (b[i] - U[i, i + 1:]@x[i + 1:])/U[i, i]

  return x
  
# eliminação gaussiana com pivotamento parcial
def gaussPivot(A, b):

  A = np.copy(A)
  b = np.copy(b)

  n = b.size

  for j in range(n - 1):
    k = np.argmax(np.abs(A[j:, j])) + j

    if(k != j):
      A[j, :], A[k, :] = A[k, :], A[j, :].copy()
      b[j], b[k] = b[k], b[j]

    for i in range(j + 1, n):
      m = A[i, j]/A[j, j]
      A[i, j:] -= m * A[j, j:]
      b[i] -= m * b[j]

  x = substRet(A, b)

  return x

x = gaussPivot(A, b)

print(x)