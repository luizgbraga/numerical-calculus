import numpy as np;
import matplotlib.pyplot as plt;

# EDO: y' = f(x, y)
# CC: y(x0) = k
# Intervalo: x0 < x < xf

# Método Trapezoidal (Heun)
def heun(f, x0, k, xf, n):
    h = (xf - x0)/n;
    x = np.arange(x0, xf + h, h);
    y = np.zeros(len(x));
    y[0] = k;
    for i in range(0, len(x) - 1):
        y[i + 1] = y[i] + h * f(x[i], y[i]);
        y[i + 1] = y[i] + (h/2) * (f(x[i], y[i]) + f(x[i + 1], y[i + 1]));
    return [x, y];

def f(x, y):
    return np.exp(x);

sis = heun(f, 0, 1, 4, 100);

plt.plot(sis[0], sis[1]);
plt.show();

