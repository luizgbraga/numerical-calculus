import numpy as np;

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