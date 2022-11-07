'''
Nome: Luiz Guilherme Amadi Braga
Número: 21414

'''

# importação das bibliotecas
import numpy as np;
import matplotlib.pyplot as plt;

# constantes e condições iniciais
S0 = 499;
I0 = 1;
R0 = 0;
T = 24;
N = 10;
m = 3;
n = 15;

# cálculo dos parâmetros
def beta(N, T, S0, I0):
    return N / (T * S0 * I0);

def gama(m, n, T): 
    return m / (n * T);

beta0 = beta(N, T, 40, 8);
gama0 = gama(m, n, T);

# precisão e intervalo
dt = 0.01;
t0 = 0;
tf = 700;
steps = int(round((tf - t0)/dt)); 

# inicializamos as soluções como np.zeros()
S_arr = np.zeros(steps + 1);
I_arr = np.zeros(steps + 1);
R_arr = np.zeros(steps + 1);
t_arr = np.zeros(steps + 1);

t_arr[0] = t0;
I_arr[0] = I0;
S_arr[0] = S0;
R_arr[0] = R0;

# método de Euler
for i in range(1, steps + 1):
    S = S_arr[i - 1];
    I = I_arr[i - 1];
    R = R_arr[i - 1];
    t = t_arr[i - 1];

    dSdt = (-1) * (beta0) * S * I;
    dIdt = (beta0) * S * I - gama0 * I;
    dRdt = gama0 * I;

    S_arr[i] = S + dt * dSdt;
    I_arr[i] = I + dt * dIdt;
    R_arr[i] = R + dt * dRdt;

    t_arr[i] = t + dt;

# plotamos o gráfico das soluções
fig = plt.figure();

plt.plot(t_arr, S_arr, linewidth=2, label='S', color='b');
plt.plot(t_arr, I_arr, linewidth=2, label='I', color='r');
plt.plot(t_arr, R_arr, linewidth=2, label='R', color='g');

plt.title('Evolução');
plt.xlabel('t');
plt.ylabel('S(t), I(t), R(t)');
plt.grid(True);
plt.axis([t0, tf, 0, 500]);

plt.legend();
plt.show();

# máximo de infectados
print(f'O máximo de infectados é {np.floor(np.max(I_arr))}');
