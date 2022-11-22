# importação das bibliotecas
import numpy as np;
import matplotlib.pyplot as plt;

a = 1;
b = -5;
c = 6;

def odesys(y0, dy, dx, x0, xf):
    steps = round((xf - x0)/dx); 
    y = [np.zeros(steps + 1) for yk in y0];
    x = np.zeros(steps + 1);
    for i in range(0, len(y)): y[i][0] = y0[i];
    for i in range(1, steps + 1):
        for j in range(0, len(y)):
            aux = [yk[i - 1] for yk in y]
            y[j][i] = aux[j] + dx * dy[j](aux); 
            x[i] = x[i - 1] + dx;
    return [x, y];

def solve2order(a, b, c, dx, x0, xf, y0):
    dy = [lambda y: y[1],
        lambda y: (-c/a) * y[0] + (-b/a) * y[1]];
    sol = odesys(y0, dy, dx, x0, xf);
    return [sol[0], sol[1][0]];

sol = solve2order(a, b, c, 0.01, 0, 2, [0, 1]);

fig = plt.figure();

plt.plot(sol[0], sol[1], color='b', label='y1');
plt.show()

