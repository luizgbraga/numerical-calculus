import numpy as np

def eigenVectors(A, eigenValues):

    A = np.array(A)
    n = A.shape[0]

    assert A.shape[1] == n, 'A matriz deve ser quadrada...'

    X = np.eye(n)
    a = np.array([1.])

    Ak = np.array(A)

    for k in range(1, n):
        ak =- Ak.trace()/k
        Ak += np.diag(np.repeat(ak, n))
        L = np.diag(eigenValues)

        X = X@L + Ak
        Ak = np.dot(A, Ak)

    for k in range(n):
        X[:,k]/= np.linalg.norm(X[:, k])

    return X
