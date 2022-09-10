import numpy as np;

# declaração da matriz A
A = np.array([[2., 4., 1.], [5., 2., 0.], [1., 1., 4.]]);

# tolerância e máximas iterações
tol = 1e-4;
maxIter = 100;

# método de Faddev-Leverrier (retorna o polinômio característico)
def faddevLeverrier(A):
    A = np.array(A);
    n = A.shape[0];

    assert A.shape[1] == n, 'A matriz deve ser quadrada...';

    a = np.array([1.]);
    Ak = np.array(A);

    for k in range(1, n + 1):

        ak = (-1) * Ak.trace() / k;
        a = np.append(a, ak);
        Ak += np.diag(np.repeat(ak, n));
        Ak = np.dot(A, Ak);

    return (-1) ** n * a;

# método de Horner
def  horner(c, z):

  n = len(c) - 1;
  b = [];
  b.append(c[0]);

  for k in range(1, n + 1):
    b.append(c[k] + b[k - 1] * z);

  y = b[n];
  q = b[:-1];

  return y, q;
  
# resolve o polinômio característico
def newtonHorner(c, r0, tol, kmax):

  n = len(c) - 1;

  raizes = [];
  iter = [];

  for k in range(n):

    niter = 0;
    r = r0;
    delta = tol + 1;
    while(niter < kmax and delta > tol):

      [pr, b] = horner(c, r);
      [dpr, b] = horner(b, r);
      rnovo = r - pr/dpr;
      delta = abs(rnovo - r);
      niter += 1;
      r = rnovo;

    [pr, c] = horner(c, r);
    raizes.append(r);
    iter.append(niter);

  return raizes, iter;

# retorna os autovetores
def eigenVectors(A, eigenValues):

    A = np.array(A);
    n = A.shape[0];

    assert A.shape[1] == n, 'A matriz deve ser quadrada...';

    X = np.eye(n);
    a = np.array([1.]);

    Ak = np.array(A);

    for k in range(1, n):
        ak =- Ak.trace()/k;
        Ak += np.diag(np.repeat(ak, n));
        L = np.diag(eigenValues);

        X = X@L + Ak;
        Ak = np.dot(A, Ak);

    for k in range(n):
        X[:,k]/= np.linalg.norm(X[:, k]);

    return X;

polCarac = faddevLeverrier(A);
eigenValues = newtonHorner(polCarac, 0, tol, maxIter)[0];

print('Autovalores: ' + str(eigenValues));

X = eigenVectors(A, eigenValues);

print('Autovetores:');
print(X);