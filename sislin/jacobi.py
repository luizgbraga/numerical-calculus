import numpy as np;

# declaração da matriz A e do vetor coluna b
A = np.array([[5., 1., 1.], [3., 4., 1.], [3., 3., 6.]]);
b = np.array([5., 6., 0.]);

# chute inicial
initialGuess = np.zeros((3));

# tolerância e iterações máximas
tol = 1e-16;
maxIter = 100;

# método de Jacobi
def jacobi(A, b, x0, tol, maxIter):

  d = np.diag(A);
  for k in range(maxIter):

    r = b - A@x0;
    h = r/d;

    if(np.linalg.norm(h) < tol + tol * np.linalg.norm(x0)):
        return x0;

    x0 += h;

  return x0;

x = jacobi(A, b, initialGuess, tol, maxIter);

print(x);