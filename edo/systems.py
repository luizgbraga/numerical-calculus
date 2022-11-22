# importação das bibliotecas
import numpy as np;
import matplotlib.pyplot as plt;

# obs.: neste exemplo, o sistema é 3x3

y0 = [499, 1, 0];
dy = [lambda y, x: -0.001302 * y[0] * y[1], 
    lambda y, x: 0.001302 * y[0] * y[1] - 0.008333 * y[1], 
    lambda y, x: 0.008333 * y[1]]
dx = 0.01;
x0 = 0;
xf = 700;

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

sol = odesys(y0, dy, dx, x0, xf);

fig = plt.figure();

plt.plot(sol[0], sol[1][0], color='b', label='y1');
plt.plot(sol[0], sol[1][1], color='g', label='y2');
plt.plot(sol[0], sol[1][2], color='r', label='y3');
plt.grid(True);
plt.axis([x0, xf, 0, 500]);

plt.legend();
plt.show();
