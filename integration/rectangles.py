import numpy as np;

# declaração da função dada
def f(x):
    return x ** 2;

# limites de integração
a = 2; 
b = 3; 

# número de intervalos (precisão)
N = 5;

def rectangle(f, a, b, N):
    deltax = (b - a)/N;
    x_medio = np.linspace(a + deltax/2, b - deltax/2, N);
    sumRec = np.sum(deltax * f(x_medio));
    return sumRec;

print(rectangle(f, a, b, N));