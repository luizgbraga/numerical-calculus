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

# substituição sucessiva (matrizes triangulares inferiores)
def substSuc(L, b):

  n = b.size
  x = np.zeros(n)

  for i in range(n):
    x[i] = (b[i] - L[i, :i]@x[:i])/L[i, i]

  return x

# decomposição LU
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

def solveLU(A, b):

  L, U = decLU(A)
  y = substSuc(L, b)
  x = substRet(U, y)

  return x

x = solveLU(A, b)

print(x)