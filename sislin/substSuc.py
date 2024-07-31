import numpy as np

# declaração da matriz triangular inferior
L = np.array([[1., 0., 0.], [2., 1., 0.], [3., 4., 1.]])

# declaração do vetor coluna b
b = np.array([1., 4., 5.])

# substituição sucessiva (matrizes triangulares inferiores)
def substSuc(L, b):

  n = b.size
  x = np.zeros(n)

  for i in range(n):
    x[i] = (b[i] - L[i, :i]@x[:i])/L[i, i]

  return x

x = substSuc(L, b)

print(x)

