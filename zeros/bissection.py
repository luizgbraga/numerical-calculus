# importa a biblioteca math
import math;

# função do método da bisseção

# recebe a função original (f), um intervalo em que com certeza há uma raiz [xMin, xMax] e a 
# tolerância para o erro da raiz (tol)

def bissection(f, xMin, xMax, tol):

    a = xMin;
    b = xMax;
    err = b - a;
    
    x_k = []; # array com os valores testados de x
    y_k = []; # array com os correspondentes f(x)

    # enquanto o erro for maior que a tolerância permitida
    while(err > tol):

        # defina x como o ponto médio do meu intervalo [a, b]
        # ou a raiz está em [a, x] ou em [x, b]
        x = (a + b)/2;

        x_k.append(x);
        y_k.append(f(x));

        # se a raiz não está em [a, x], o meu novo a será meu x
        if(f(x) * f(a) > 0):
            a = x;
        # se está em [a, x], meu novo b será meu x
        else:
            b = x;
        err = b - a;

    print(x_k);
    print(y_k);

    return [x, err];

def f(x): 
    return math.cos(x) + x;

root_f = bissection(f, -10, 10, 0.01)[0];
error = bissection(f, -10, 10, 0.01)[1];

print('A raiz de f vale ' + str(root_f) + ', com erro ' + str(error));

