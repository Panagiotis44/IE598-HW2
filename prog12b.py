import numpy as np
import random

def create_random_matrices():
    m = random.randint(2, 20)
    n = random.randint(2, 20)
    A = np.random.random((m, n))  # Generates random matrix A
    B = np.random.random((m, n))  # Generates random matrix B
    return A, B

def find_pure_nash_equilibrium(A, B):
    m, n = A.shape

    # Check for pure Nash equilibrium
    for i in range(m):
        for j in range(n):
            row_payoff = A[i, j]
            col_payoff = B[i, j]

            # Check if (i, j) is a pure Nash equilibrium
            is_nash_eq = True
            for k in range(m):
                if k != i and A[k, j] > row_payoff:
                    is_nash_eq = False
                    break
            for l in range(n):
                if l != j and B[i, l] > col_payoff:
                    is_nash_eq = False
                    break

            if is_nash_eq:
                return (i, j)

    return None

count_ne = 0
for i in range(1000):
    # Create random matrices A and B
    A, B = create_random_matrices()

    #print("Matrix A:")
    #print(A)
    #print("Matrix B:")
    #print(B)

    # Find pure Nash equilibrium

    nash_eq = find_pure_nash_equilibrium(A, B)
    if nash_eq:
        #print("Pure Nash equilibrium exists at strategy profile:", nash_eq)
        count_ne+=1

print("number of NE: ",count_ne)
