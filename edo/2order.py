# importação das bibliotecas
import numpy as np;
import matplotlib.pyplot as plt;

# y'' + P(x)y' + Q(x)y = F(x)

def P(x): return 0;
def Q(x): return x ** 2;
def F(x): return 0;

dy = [P, Q, F];

def odesys(y0, dy, dx, x0, xf):
    steps = round((xf - x0)/dx); 
    y = [np.zeros(steps + 1) for yk in y0];
    x = np.zeros(steps + 1);
    for i in range(0, len(y)): y[i][0] = y0[i];
    for i in range(1, steps + 1):
        for j in range(0, len(y)):
            aux = [yk[i - 1] for yk in y]
            y[j][i] = aux[j] + dx * dy[j](aux, x[i]); 
            x[i] = x[i - 1] + dx;
    return [x, y];

def solve2order(y0, P, Q, F, dx, x0, xf):
    dy = [lambda y, x: y[1],
        lambda y, x: F(x) - Q(x) * y[0] - P(x) * y[1]];
    sol = odesys(y0, dy, dx, x0, xf);
    return [sol[0], sol[1][0]];

sol = solve2order([0, 1], P, Q, F, 0.01, 0, 10);

fig = plt.figure();

plt.plot(sol[0], sol[1], color='b', label='y1');
plt.show()

