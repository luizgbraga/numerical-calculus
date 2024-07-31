'''

VC CNU: 14/09/2022 - Questão 5 - TC R. Gomes
Nome: Luiz Guilherme Amadi BRAGA
Número: 21414
Turma A

'''

# importações das bibliotecas
import pandas as pd
import matplotlib.pyplot as plt

# declaração da função dada
def p(d, t):
    if(d == 0): return 1 # P_0
    elif(d == 1): return t # P_1
    else:
        a = (2 * (d - 1) + 1)/((d - 1) + 1)
        b = (-1) * ((d - 1)/((d - 1) + 1))

        return a * t * p((d - 1), t) + b * p((d - 1) - 1, t)

# arredondamento de n casas decimais
n = 4

# tolerância e máximas iterações
tol = 0.0000001
maxIter = 1000

# método da bisseção
def bissection(f, d, xMin, xMax, tol, maxIter):

    i = 0
    a = xMin
    b = xMax
    err = b - a

    if(f(d, a) * f(d, b) > 0):
        return 'error'

    while((err > tol) and (i < maxIter)):

        x = (a + b)/2

        if(f(d, x) * f(d, a) < 0):
            b = x
        elif(f(d, x) * f(d, b) < 0):
            a = x
        elif(f(d, x) == 0):
            return x

        err = b - a
        i += 1

    return x


# lista de objetos que contém o dia da semana e uma array com intervalos [xMin, xMax] nos quais há raízes positivas
# todos os intervalos foram verificados graficamente

dias = [{ 'dia': 'Segunda-feira', 'intervals': [[0, 1]] },
        { 'dia': 'Terça-feira', 'intervals': [[-1, 1]] }, 
        { 'dia': 'Quarta-feira', 'intervals': [[0, 1]] }, 
        { 'dia': 'Quinta-feira', 'intervals': [[-0.25, 0.25], [0.5, 1]] }, 
        { 'dia': 'Sexta-feira', 'intervals': [[0.2, 0.6], [0.6, 1]] }, 
        { 'dia': 'Sábado', 'intervals': [[-0.25, 0.25], [0.3, 0.6], [0.75, 1]] }, 
        { 'dia': 'Domingo', 'intervals': [[0, 0.5], [0.5, 0.8], [0.8, 1]] }]

tabela = []

for d in range(0, 7):

    horas = []

    for interval in dias[d]['intervals']:
        root = bissection(p, d, interval[0], interval[1], tol, maxIter)
        if(root == 'error'): horas.append('Não há raizes')
        else: horas.append(round(root, n))

    myData = pd.Series({ 'Dia': dias[d]['dia'], 'Horas': horas })
    tabela.append(myData)

df = pd.DataFrame(tabela)
print(df)
