import numpy as np;

def Gauss_Seidel(A,b,initial_guess):
    #Decomposing matrix A into a lower triangle matrix and a strictly upper triangle matrix:
    L = np.tril(A)
    U = np.triu(A,1)
    #Calculating the inverse of matrix L:
    L_inv = np.linalg.inv(L)
    
    #Symbol of matrix multiplication in numpy is @
    T = -L_inv@U
    C = L_inv@b
    x = initial_guess

    
    while(1):
        x_old = x
        x = T@x + C
        x_new = x
        #using norm2:
        if np.linalg.norm(x_new-x_old) < 10**(-4):
            break
    return x

A = np.matrix([[2.0,1.0],
               [5.0,7.0]])
b = np.matrix([[11.0],[13.0]])
initialGuess = np.matrix([[1.0],[1.0]])

sol = Gauss_Seidel(A,b,initialGuess)

print ('A:')
print(A)

print ('\nb:')
print(b)

print('\nSolution:')
print(sol)