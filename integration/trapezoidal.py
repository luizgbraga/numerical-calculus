import numpy as np

# declaração da função dada
def f(x):
    return x ** 2

# limites de integração
a = 2 
b = 3 

k = 21
tol = 1e-5

def trapezio(f, a, b, I0, k, tol):
    if k == 1: 
        I = (f(a) + f(b))*(b - a)/2.0
    else:
        N = 2**(k - 2)
        deltax = (b - a)/N
        x = a + deltax/2.0
        sumTrap = 0.0
        for i in range(N):
            sumTrap += f(x)
            x += deltax
        I = (I0 + deltax * sumTrap)/2.0
    return I

def calculate(f, a, b, I0, k, tol):
    for i in range(1, k):
        I = trapezio(f, a, b, I0, i, tol)
        if (i > 1) and (abs(I - I0)) < tol: break
        I0 = I
    return I

print(calculate(f, a, b, 0, k, tol))