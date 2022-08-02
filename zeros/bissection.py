# importa a biblioteca math
import math;

# função do método da bisseção

# esse método se baseia no fato de que se f(a) * f(b) < 0, com certeza há uma raiz em [a, b]

# recebe a função original (f), um intervalo em que com certeza há uma raiz [xMin, xMax] e a 
# tolerância para o erro da raiz (tol)

def bissection(f, xMin, xMax, tol):

    a = xMin;
    b = xMax;
    err = b - a; # erro => tamanho do intervalo em que temos certeza de que há uma raiz
    
    x_k = []; # array com os valores testados de x
    y_k = []; # array com os correspondentes f(x)

    # enquanto o erro for maior que a tolerância permitida
    while(err > tol):

        # defina x como o ponto médio do meu intervalo [a, b]
        # ou a raiz está em [a, x] ou em [x, b]
        x = (a + b)/2;

        # esse pedaço é só para adicionar os valores que testamos de x e f(x) em arrays, para controle (não obrigatório)
        x_k.append(x);
        y_k.append(f(x));

        # a lógica é: se f(x) * f(a) for menor que 0, a raiz ESTÁ nesse NOVO intervalo [a, x]
        # então podemos aplicar esse método novamente, mas para uma BISSEÇÃO do meu intervalo
        # e então seguimos dividindo meu intervalo em dois, sempre escolhendo a bisseção que podemos garantir a existência da raiz

        # se a raiz não está em [a, x], o meu novo a será meu x
        if(f(x) * f(a) > 0):
            a = x;
        # se está em [a, x], meu novo b será meu x
        else:
            b = x;
        err = b - a;

    # print das arrays de controle
    print(x_k);
    print(y_k);

    return [x, err];


# função em questão que quero achar a raiz
def f(x): 
    return math.cos(x) + x;

root_f = bissection(f, -10, 10, 0.01)[0];
error = bissection(f, -10, 10, 0.01)[1];

# str(number) só transforma um número em string

print('A raiz de f vale ' + str(root_f) + ', com erro ' + str(error));

