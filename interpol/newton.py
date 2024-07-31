import numpy as np
import numpy.polynomial.polynomial as poly
import matplotlib.pyplot as plt
import pandas as pd

# pontos em que sabemos o valor da função
x = np.array([1, 2, 3, 4])
y = np.array([1, 2, 3, 4])

# pontos em que queremos estender a função
xNovos = np.linspace(1, 10)

def newton(x, y, xNovos):

  N = len(y)
  DD = np.zeros([N, N])
   
  DD[:, 0] = y
  for j in range(1, N):
    for i in range(N - j):
      DD[i, j] = (DD[i + 1,j - 1] -DD[i, j - 1])/(x[i + j] - x[i])

  a = DD[0, :]
  n = a[N - 1]

  for k in reversed(range(N - 1)):
    n = a[k] + (xNovos -x[k]) * n

  return n, DD

y_novos, DD = newton(x, y, xNovos)

print(DD)
plt.figure(figsize = (12, 8))

plt.plot(x, y, "ro")
plt.plot(xNovos, y_novos)
plt.show()