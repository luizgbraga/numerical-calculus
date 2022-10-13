import numpy as np;
import matplotlib.pyplot as plt;

def f(t):
    if(t > 0 and t < 0.5): return 2;
    elif(t > 0.5 and t < 1): return 1;
    else: return 0;

def integrating(t, s, z):
    num = z * f(t);
    den = ((z ** 2 + (s - t) ** 2)) ** (3/2);
    return num/den;

def rectangle(f, a, b, N, s, z):
    deltax = (b - a)/N;
    xMedio = np.linspace(a + deltax/2, b - deltax/2, N);
    sumRec = np.sum([deltax * f(x, s, z) for x in xMedio]);
    return sumRec;

zValues = [0.25, 0.5, 1];
sMin = 0;
sMax = 2;

for z in zValues:
    sValues = np.linspace(sMin, sMax, 100);
    gValues = [rectangle(integrating, 0, 1, 10, s, z) for s in sValues];
    plt.plot(sValues, gValues);
    plt.show();