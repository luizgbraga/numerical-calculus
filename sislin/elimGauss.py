import numpy as np;

# declaração da matriz A e do vetor coluna b
A = np.array([[2., 4., 1.], [5., 2., 0.], [1., 1., 4.]]);
b = np.array([1., 0., 0.]);

# substituição sucessiva (matrizes triangulares superiores)
def substRet(U, b):

  n = b.size;
  x = np.zeros(n);

  for i in reversed(range(n)):
    x[i] = (b[i] - U[i, i + 1:]@x[i + 1:])/U[i, i];

  return x;

def elimGauss(A, b):

  A = np.copy(A);
  b = np.copy(b);
  n = b.size;

  for j in range(n - 1):
    for i in range(j + 1, n):
        if(A[j][j] != 0):
            m = A[i, j]/A[j, j];
            A[i, j:] -= m * A[j, j:];
            b[i] -= m * b[j];

    for i in range(0, n):
        if(b[i] != 0 and A[i][-1] == 0):
            print('SI');
            return;

    for i in range(0, n):
        if(b[i] == 0 and A[i][-1] == 0):
            print('SPI');
            return;

  x = substRet(A, b);

  return x;

x = elimGauss(A, b);

print(x);