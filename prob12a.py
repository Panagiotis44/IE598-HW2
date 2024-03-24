import numpy as np
import random

def create_random_matrices():
    m = random.randint(2, 20)
    n = random.randint(2, 20)

    A = np.random.random((m, n))  # Generates random matrix A
    B = np.random.random((m, n))  # Generates random matrix B

    return A, B

def find_pure_nash_equilibria(A, B):
    m, n = A.shape
    nash_equilibria = []

    # Check for pure Nash equilibria
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
                nash_equilibria.append((i, j))

    return nash_equilibria


# Create random matrices A and B
A, B = create_random_matrices()

print("Matrix A:")
print(A)
print("Matrix B:")
print(B)

# Find all pure Nash equilibria
nash_equilibria = find_pure_nash_equilibria(A, B)
if nash_equilibria:
    print("Pure Nash equilibria:")
    for eq in nash_equilibria:
        print("  Strategy profile:", eq)
else:
    print("No pure Nash equilibrium exists.")

