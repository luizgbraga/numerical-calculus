import numpy as np

# declaração da matriz A
A = np.array([[2., 4., 1.], [5., 2., 0.], [1., 1., 4.]])

# método de Faddev-Leverrier
def faddevLeverrier(A):
    A = np.array(A)
    n = A.shape[0]

    assert A.shape[1] == n, 'A matriz deve ser quadrada...'

    a = np.array([1.])
    Ak = np.array(A)

    for k in range(1, n + 1):

        ak = (-1) * Ak.trace() / k
        a = np.append(a, ak)
        Ak += np.diag(np.repeat(ak, n))
        Ak = np.dot(A, Ak)

    return (-1) ** n * a

polCarac = faddevLeverrier(A)

for i in range(0, A.shape[0] + 1):
    print(str(polCarac[i]) + '* x ^ ' + str(i))