from mimetypes import init
import numpy as np;

# declaração da matriz A e do vetor coluna b
A = np.array([[5., 1., 1.], [3., 4., 1.], [3., 3., 6.]]);
b = np.array([5., 6., 0.]);

# chute inicial
initialGuess = np.zeros((3));

# tolerância e iterações máximas
tol = 1e-16;
maxIter = 100;

# substituição sucessiva (matrizes triangulares inferiores)
def substSuc(L, b):

  n = b.size;
  x = np.zeros(n);

  for i in range(n):
    x[i] = (b[i] - L[i, :i]@x[:i])/L[i, i];

  return x;

# método de Gauss-Seidel
def gaussSeidel(A, b, x0, tol, maxIter):

  M = np.tril(A);

  for k in range(maxIter):

    r = b - A@x0;
    h = substSuc(M,r);

    if(np.linalg.norm(h) < tol + tol * np.linalg.norm(x0)):
      break;

    x0 += h;

  return x0;

x = gaussSeidel(A, b, initialGuess, tol, maxIter);

print(x);