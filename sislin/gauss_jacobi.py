import numpy as np;

def jacobi(A,b,initial_guess):
    #Extracting Diagonal elements from input matrix A:
    Diagnal = np.diag(A)
    D = np.diagflat(Diagnal)
    
    #Calculating Invese of D:
    D_inv = np.linalg.inv(D)
    
    #Calculating R:
    R = A - D
    
    #Symbol of matrix multiplication in numpy is @
    T = -D_inv@R
    C = D_inv@b
    x = initial_guess

    while(1):
        x_old = x
        x = T@x + C
        x_new = x
        #using norm2:
        if np.linalg.norm(x_new-x_old) <= 10**(-4):
            break
    return x;

A = np.matrix([[2.0,1.0],
               [5.0,7.0]])

b = np.matrix([[11.0],[13.0]])

initialGuess = np.matrix([[1.0],[1.0]])

sol = jacobi(A,b,initialGuess)

print ('A:')
print(A)

print ('\nb:')
print(b)

print('\nSolution:')
print(sol)