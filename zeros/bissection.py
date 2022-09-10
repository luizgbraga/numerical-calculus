import numpy as np;

# declaração da função dada
def f(x): 
    return x ** 2 - 4;

# intervalo analisado
initialValue = 1;
finalValue = 3;

# tolerância e máximas iterações
tol = 0.001;
maxIter = 10;

# método da bisseção
def bissection(f, xMin, xMax, tol, maxIter):

    i = 0;
    a = xMin;
    b = xMax;
    err = b - a;

    if(f(a) * f(b) > 0):
        print('f(a) and f(b) must have opposite signals');
        return [0, 0];

    while((err > tol) and (i < maxIter)):

        x = (a + b)/2;

        if(f(x) * f(a) < 0):
            b = x;
        elif(f(x) * f(b) < 0):
            a = x;
        elif(f(x) == 0):
            return [x, 0];

        err = b - a;
        i += 1;

    return x;

root = bissection(f, initialValue, finalValue, tol, maxIter);

print('Método da bisseção: a raiz vale ' + str(root));
