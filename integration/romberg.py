import numpy as np;

# declaração da função dada
def f(x):
    return x ** 2;

# limites de integração
a = 2; 
b = 3; 

k = 21;
tol = 1e-5;

def richardson(r, k):
    for j in range(k - 1, 0, -1):
      const = 4.0**(k - j);
      r[j] = (const * r[j + 1] - r[j])/(const - 1.0);
    return r;

def trapezio(f, a, b, I0, k, tol):
    if k == 1: 
        I = (f(a) + f(b))*(b - a)/2.0;
    else:
        N = 2**(k - 2);
        deltax = (b - a)/N;
        x = a + deltax/2.0;
        sumTrap = 0.0;
        for i in range(N):
            sumTrap += f(x);
            x += deltax;
        I = (I0 + deltax * sumTrap)/2.0;
    return I;

def romberg(f, a, b, tol):
    r = np.zeros(21);
    r[1] = trapezio(f, a, b, 0.0, 1, tol);
    R = r[1];
    for k in range(2, 21):
        r[k] = trapezio(f, a, b, r[k - 1], k, tol);
        r = richardson(r, k);
        if abs(r[1] - R) < tol * max(abs(r[1]), 1.0):
            return r[1];
        R = r[1];
    print("Romberg não convergiu");

print(romberg(f, a, b, tol));