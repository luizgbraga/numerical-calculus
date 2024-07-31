import numpy as np

# declaração da matriz A
A = np.array([[2., 4., 1.], [5., 2., 0.], [1., 1., 4.]])

# máximas iterações
maxIter = 100

# transformação de Householder
def householder(x, k):

  n = x.size
  w = np.zeros(n)

  sum = x[k+1 :]@x[k+1 :]
  gk = np.sqrt(x[k] ** 2 + sum)
  c = np.sqrt((x[k] + gk) ** 2 + sum)
  w[k] = (x[k] + gk)/c
  w[k + 1 :] = x[k + 1 :]/c
  H = np.eye(n) - 2 * np.outer(w, w.T)

  return H

# decomposição QR
def decQR(A):

  n = A.shape[0]
  R = np.copy(A)
  Q = np.eye(n)
  
  for k in range(n - 1):
    H = householder(R[:, k], k)

    R = H @ R
    Q = Q @ H

  return Q, R

# resolve
def QRmethod(A, maxIter):
  
  T = np.copy(A)

  for k in range(maxIter):
    Q, R = decQR(T)
    T = R @ Q

  eigenvalues = np.diag(T)

  return eigenvalues

x = QRmethod(A, maxIter)

print(x)