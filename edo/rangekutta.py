import numpy as np;
import matplotlib.pyplot as plt;

# EDO: y' = f(x, y)
# CC: y(x0) = k
# Intervalo: x0 < x < xf

# Range-Kutta de 2ª ordem
def rangekutta2(f, x0, k, xf, n):
    h = (xf - x0)/n;
    x = np.arange(x0, xf + h, h);
    y = np.zeros(len(x));
    y[0] = k;
    for i in range(0, len(x) - 1):
        y[i + 1] = y[i] + (h/2) * (f(x[i], y[i]) + f(x[i] + h, y[i] + h * f(x[i], y[i])));
    return [x, y];

# Range-Kutta de 4ª ordem
def rangekutta4(f, x0, k, xf, n):
    h = (xf - x0)/n;
    x = np.arange(x0, xf + h, h);
    y = np.zeros(len(x));
    y[0] = k;
    for i in range(0, len(x) - 1):
        y1 = h * f(x[i], y[i]);
        y2 = h * f(x[i] + h/2, y[i] + y1/2);
        y3 = h * f(x[i] + h/2, y[i] + y1/2);
        y4 = h * f(x[i] + h, y[i] + y3);
        y[i + 1] = y[i] + (y1 + 2 * (y2 + y3) + y4)/6;
    return [x, y];

def f(x, y):
    return np.exp(x);

sis = rangekutta2(f, 0, 1, 4, 100);

plt.plot(sis[0], sis[1]);
plt.show();