import numpy as np;
import numpy.polynomial.polynomial as poly;
import matplotlib.pyplot as plt;
import pandas as pd;

def newton(x, y, x_novos):

  N = len(y);
  DD = np.zeros([N, N]);
   
  DD[:, 0] = y;
  for j in range(1, N):
    for i in range(N - j):
      DD[i, j] = (DD[i + 1,j - 1] -DD[i, j - 1])/(x[i + j] - x[i]);

  a = DD[0, :];
  n = a[N - 1];

  for k in reversed(range(N - 1)):
    n = a[k] + (x_novos -x[k]) * n;

  return n, DD;

x = np.array([-5, -1, 0, 2]);
y = np.array([-2, 6, 1, 3]);

x_novos = np.arange(-5, 2.1, .1);
y_novos,DD = newton(x, y, x_novos);

print(DD);
plt.figure(figsize = (12, 8));

plt.plot(x, y, "ro");
plt.plot(x_novos, y_novos);
plt.show();