import numpy as np 

# declaração da função dada
def f(x):
    return x + np.cos(x)

# chute inicial
initialGuess = 0.8

# tolerância e máximas iterações
tol = 0.001
maxIter = 10

# método de Steffesen
def steffesen(f, x0, tol, maxIter):

    def g(x):
        return (f(x + f(x))/f(x)) - 1

    i = 0
    x_k = [x0]
    y_k = [f(x0)]

    while(abs(f(x_k[-1])) > tol or i > maxIter):

        next_x = x_k[-1] - f(x_k[-1])/g(x_k[-1])
        
        x_k.append(next_x)
        y_k.append(f(next_x))

    # print(x_k)
    # print(y_k)    

    return x_k[-1]

root = steffesen(f, initialGuess, tol, maxIter)

print('Método de Steffesen: a raiz vale ' + str(root))
