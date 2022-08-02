# importa a biblioteca math
import math;

# É IGUAL A BISSEÇÃO, MAS NÃO É MAIS BISSEÇÃO
# agora o x é uma média ponderada de a e b, não mais uma média aritmética
# a lógica é a mesma

# função do método da falsa posição
# é idêntica ao método da bisseção, só muda que em vez do x ser uma média aritmética, será ponderada

# recebe a função original (f), um intervalo em que com certeza há uma raiz [xMin, xMax] e a 
# tolerância para o erro da raiz (tol)

def false_pos(f, xMin, xMax, tol):

    a = xMin;
    b = xMax;
    err = b - a;
    
    x_k = [];
    y_k = [];

    while(err > tol):

        # calcula x como a média ponderada
        # de resto, idêntico à bisseção
        x = (a * abs(f(b)) + b * abs(f(a)))/(abs(f(a)) + abs(f(b)));

        x_k.append(x);
        y_k.append(f(x));

        if(f(x) * f(a) > 0):
            a = x;
        else:
            b = x;
        err = b - a;

    print(x_k);
    print(y_k);

    return [x, err];

def f(x): 
    return math.cos(x) + x;

root_f = false_pos(f, -10, 10, 0.1)[0];
error = false_pos(f, -10, 10, 0.1)[1];

print('A raiz de f vale ' + str(root_f) + ', com erro ' + str(error));
