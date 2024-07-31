# importação das bibliotecas
import numpy as np
import matplotlib.pyplot as plt

# y'' + P(x)y' + Q(x)y = F(x)

def odesys(y0, dy, dx, x0, xf):
    steps = round((xf - x0)/dx) 
    y = [np.zeros(steps + 1) for yk in y0]
    x = np.zeros(steps + 1)
    for i in range(0, len(y)): y[i][0] = y0[i]
    for i in range(1, steps + 1):
        for j in range(0, len(y)):
            aux = [yk[i - 1] for yk in y]
            y[j][i] = aux[j] + dx * dy[j](aux, x[i]) 
            x[i] = x[i - 1] + dx
    return [x, y]

def solve2order(y0, P, Q, F, dt, t0, tf):
    dy = [lambda y, t: y[1],
        lambda y, t: F(y[0]) - Q(t) * y[0] - P(t) * y[1]]
    sol = odesys(y0, dy, dt, t0, tf)
    return [sol[0], sol[1][0]]


# dados do problema
g, R = 9.81, 6370000

def P(t): return 0
def Q(t): return 0
def F(x): return -g * (R ** 2)/((R + x) ** 2)

sol = solve2order([0, 1500], P, Q, F, 0.01, 0, 300)

maxValue = np.max(sol[1])
i = np.where(sol[1] == maxValue)
maxTime = sol[0][i]

print('No tempo {} s, a altura é máxima igual a {}'.format(maxTime, maxValue))

fig = plt.figure()

plt.plot(sol[0], sol[1], color='b', label='y1')
plt.show()
