# importação das bibliotecas
import numpy as np;
import matplotlib.pyplot as plt;

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

# condições de cada problema

# y0 = [y1(x0), y2(x0), y3(x0), ...]
y0 = [499, 1, 0];

# dy = [y1', y2', y3', ...] (ver observação 2 e 3)
dy = [lambda y, x: -0.001302 * y[0] * y[1], 
    lambda y, x: 0.001302 * y[0] * y[1] - 0.008333 * y[1], 
    lambda y, x: 0.008333 * y[1]]

# tamanho do intervalo (precisão)
dx = 0.01;

# intervalo de x
x0 = 0;
xf = 700;

sol = odesys(y0, dy, dx, x0, xf);

fig = plt.figure();

plt.plot(sol[0], sol[1][0], color='b', label='y1');
plt.plot(sol[0], sol[1][1], color='g', label='y2');
plt.plot(sol[0], sol[1][2], color='r', label='y3');
plt.grid(True);
plt.axis([x0, xf, 0, 500]);

plt.legend();
plt.show();


'''

Observações:
1. A função odesys resolve sistemas genéricos N x N
2. A única restrição é: (y_i)' = f(x, y_1, y_2, ..., y_n)
2a. Ou seja, as derivadas não podem ser funções de outras derivadas
2b. Mas pode ser função de quaisquer y_k e também de x
3. Talvez a maior dificuldade desse código seja a array dy
3a. A array dy é uma array de funções
3b. Cada função dessa array corresponde a um (y_i)'
3c. Cada função tem como argumento y = [y1, y2, ...] e x
3d. Portanto, quando definimos a função, y1 = y[0], y2 = y[1], ...

'''