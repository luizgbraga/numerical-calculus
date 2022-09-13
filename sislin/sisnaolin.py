import numpy as np;

# tolerância e iterações máximas
tol = 1e-16;
maxIter = 100;

# funções do sistema não-linear f[0] e f[1]
def f(x):
  f = np.zeros(len(x));

  f[0] = (4) * (np.sin(x[0]) * np.sin(x[1]) + np.cos(x[0]) * np.cos(x[1]) - 10);
  f[1] = (np.sin(x[0]) * np.sin(x[1]) + np.cos(x[0]));
  return f;

# substtuição retroativa
def substRet(U, b):

  n = b.size;
  x = np.zeros(n);

  for i in reversed(range(n)):
    x[i] = (b[i] - U[i, i + 1:]@x[i + 1:])/U[i, i];

  return x;


# eliminação com pivotamento
def gaussPivot(A, b):

  A = np.copy(A);
  b = np.copy(b);

  n = b.size;

  for j in range(n - 1):
    k = np.argmax(np.abs(A[j:, j])) + j;

    if(k != j):
      A[j, :], A[k, :] = A[k, :], A[j, :].copy();
      b[j], b[k] = b[k], b[j];

    for i in range(j + 1, n):
      m = A[i, j]/A[j, j];
      A[i, j:] -= m * A[j, j:];
      b[i] -= m * b[j];

  x = substRet(A, b);

  return x;


# resolução por Newton_Raphson
def newtonRaphsonSis(f, x, tol, maxIter):

  def jacobiana(f, x):
    h = 1.0e-4;
    n = len(x);
    J = np.zeros((n,n));
    f0 = f(x);

    for i in range(n):
      x_original = x[i];
      x[i] = x_original + h;

      f1 = f(x);
      x[i] = x_original;
      J[:, i] = (f1 - f0)/h;

    return J, f0;

  for k in range(maxIter):

    J, f0 = jacobiana(f, x);
    if np.linalg.norm(f0)/len(x) < tol: return x;
    dx = gaussPivot(J, -f0);
    x += dx;
    if np.linalg.norm(dx) < tol * max(max(abs(x)), 1.0):
      break;
  print('não convergiu');

  return x;

x0 = np.array([np.deg2rad(20), np.deg2rad(-20)]);

x = newtonRaphsonSis(f, x0, tol, maxIter);


print(x);