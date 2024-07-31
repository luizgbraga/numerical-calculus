import numpy as np 

# declaração da função dada
def f(x):
    return x + np.cos(x)

# derivada de f
def dfdx(x): 
    return 1 - np.sin(x)

# chute inicial
initialGuess = 0.8

# tolerância e máximas iterações
tol = 0.001
maxIter = 10

# método de Newton-Raphson
def newtonRaphson(f, dfdx, x0, tol, maxIter):

    i = 0
    x_k = [x0]
    y_k = [f(x0)]

    while(abs(f(x_k[-1])) > tol or i > maxIter):

        next_x = x_k[-1] - f(x_k[-1])/dfdx(x_k[-1])
        
        x_k.append(next_x)
        y_k.append(f(next_x))

    # print(x_k)
    # print(y_k)    

    return x_k[-1]

root = newtonRaphson(f, dfdx, initialGuess, tol, maxIter)

print('Método de Newton-Raphson: a raiz vale ' + str(root))
