# importa o a biblioteca math
import math;

# função do método do ponto fixo

# recebe a função original (f), a função de iteração (phi), o chute inicial (x0) a tolerância de erro
# para o zero (tol), a quantidade máxima de iterações (max_iter)

def mpf(f, phi, x0, tol, max_iter):

    x_k = [x0]; # cria uma array que será a sequência x_k
    k = 0; # vai contar as iterações

    # enquanto o valor absoluto de f(x) for maior que a tolerância (queremos que seja 0 -> raiz) e o k não passar as iterações máximas
    while(abs(f(x_k[-1])) > tol and k < max_iter):

        # o próximo x será a função de iteração phi aplicada no último x
        x_next = phi(x_k[-1]);

        # adicionamos esse cara na sequência
        x_k.append(x_next);
        k += 1;

    return x_k;

def f(x):
    return x ** 2 -(math.e) ** x;

def phi(x):
    return (-1) * math.sqrt((math.e) ** x);

root_f = mpf(f, phi, -1, 0.001, 20);
print('A raiz de f vale ' + str(root_f[-1]));