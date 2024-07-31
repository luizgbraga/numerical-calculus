import numpy as np

# declaração da função dada
def f(x):
    return x ** 2 - (np.e) ** x

# função de iteração
def phi(x):
    return (-1) * np.sqrt((np.e) ** x)

# chute inicial
initialGuess = -1

# tolerância e máximas iterações
tol = 0.001
maxIter = 10

# método do ponto fixo
def mpf(f, phi, x0, tol, maxIter):

    x_k = [x0]
    k = 0

    while(abs(f(x_k[-1])) > tol and k < maxIter):

        x_next = phi(x_k[-1])
        x_k.append(x_next)
        k += 1

    return x_k[-1]


root = mpf(f, phi, initialGuess, tol, maxIter)

print('Método do ponto fixo: a raiz vale ' + str(root))
