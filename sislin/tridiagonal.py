import numpy as np;

# 'diagonais'
d = np.array([1, 4, 3, 5, 7]);
c = np.array([0, 3, 2, 1, 1]);
e = np.array([1, 3, 2, 3, 0]);

# vetor coluna
b = np.array([5.0, -5.0, 4.0, -5.0, 5.0]);

# resolve sistema com as 'diagonais' c, d, e (subindo)
def solveTridiagonal(c, d, e, b):

  n = len(d);
  k = np.ones((n));
  t = np.ones((n)); 
  x = np.ones((n));

  for i in range(n):
    dem = d[i] - c[i] * t[i - 1];
    k[i] =(b[i] - c[i] * k[i - 1])/dem;
    t[i] = e[i]/dem;

  x[n - 1] = k[n - 1];

  for i in reversed(range(n - 1)):
    x[i] = k[i] - t[i] * x[i + 1];

  return x;

x = solveTridiagonal(c, d, e, b);

print(x);  
  
           