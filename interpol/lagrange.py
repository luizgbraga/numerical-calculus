import numpy as np;
import numpy.polynomial.polynomial as poly;
import pandas as pd;

def lagrange(x, y):

  n = len(x);
  l = np.zeros(n);
  P = [];
  L = np.zeros((n,n));

  for m in range(n):
    P = [1];
    for k in range(n):
      if (k != m): 
        P = poly.polymul(P,[-x[k], 1])/(x[m] - x[k]);

    L[m, :] = P;
    l = l + y[m] * P;    

  return l, L;

x = [-1, 0, 3];
y = [15, 8,-1];

l, L = lagrange(x, y);

Tabela = pd.DataFrame(L);

print(l);
print(Tabela);