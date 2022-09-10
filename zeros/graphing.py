import numpy as np; 
import matplotlib.pyplot as plt;

# declaração da função dada
def f(x): 
    return x ** 2 - 4;

# intervalo analisado
initialValue = -1;
finalValue = 3;

x = np.linspace(initialValue, finalValue);
y = [f(a) for a in x];

plt.plot(x, y);
plt.show();