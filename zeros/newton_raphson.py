# importa a biblioteca numpy
import numpy as np;

def f(x):
    return np.cos(x) - 2 * x ** 3;

def dfdx(x): 
    return (-1) * np.sin(x) - 6 * x ** 2;

# função do método de Newton-Raphson

# esse método se aproxima da raiz ao ver onde a reta tangente a um ponto inicial de chute cruza as abcissas
# usamos y - y0 = m(x - x0) => y - f(x0) = dfdx(x0) * (x - x0) => fazemos y = 0, para ver onde cruza =>
# -f(x0) = dfdx(x0) * x - dfdx(x0) * x0 => x = x0 - f(x0)/dfdx(x0)

# recebe a função original (f), sua derivada (dfdx), o chute inicial (x0), a tolerância (tol) e
# a quantidade máxima de iterações (max_iter)

def newton_raphson(f, dfdx, x0, tol, max_iter):

    i = 0; # vai contar as iterações

    x_k = [x0]; # array com os valores testados de x
    y_k = [f(x0)]; # array com os correspondentes f(x)

    while(abs(f(x_k[-1])) > tol or i > max_iter):

        # método para calcular o próximo valor de x
        # é onde a reta tangente em x0 cruza as abcissas
        next_x = x_k[-1] - f(x_k[-1])/dfdx(x_k[-1]);
        
        x_k.append(next_x);
        y_k.append(f(next_x));

    print(x_k);
    print(y_k);    

    return x_k[-1];

root_f = newton_raphson(f, dfdx, 2, 0.001, 1000);
print('A raiz de f vale ' + str(root_f));
