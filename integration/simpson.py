import numpy as np

# declaração da função dada
def f(x):
    return x ** 2

# limites de integração
a = 2 
b = 3 

# número de intervalos (precisão)
N = 5

def simpson(f, a, b, n):
  h = (b - a)/(n - 1)
  x = a + np.arange(n) * h
  A = 2 * np.ones(n)
  A[1::2] = 4 
  A[0] = 1 
  A[-1] = 1
  parcela = A * f(x)
  return (h/3) * np.sum(parcela)

print(simpson(f, a, b, N))