# importação de bibliotecas
import numpy as np 

# declaração da função dada
def f(x):
    return x + np.cos(x)

# intervalo analisado
initialValue = 1
finalValue = 3

# tolerância e máximas iterações
tol = 0.001
maxIter = 10

# método da secante
def secante(f, xMin, xMax, tol, maxIter):

    i = 0
    a = xMin
    b = xMax

    while(((abs(b - a) > tol) or (abs(f(b)) > tol)) and (i < maxIter)):

        m = (f(b) - f(a))/(b - a)
        next_x = b - f(b)/m

        a = b
        b = next_x
        
        i += 1

    return b

root = secante(f, initialValue, finalValue, tol, maxIter)

print('Método da secante: a raiz vale ' + str(root))
