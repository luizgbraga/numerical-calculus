import numpy as np;

# declaração da matriz triangular superior
U = np.array([[5., 6., 1.], [0., 7., 2.], [0., 0., 1.]]);

# declaração do vetor coluna b
b = np.array([1., 4., 5.]);

# substituição sucessiva (matrizes triangulares superiores)
def substRet(U, b):

  n = b.size;
  x = np.zeros(n);

  for i in reversed(range(n)):
    x[i] = (b[i] - U[i, i + 1:]@x[i + 1:])/U[i, i];

  return x;

x = substRet(U, b);

print(x);