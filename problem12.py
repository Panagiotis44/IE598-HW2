def find_pure_nash_equilibria(matrix_A, matrix_B):
    m, n = len(matrix_A), len(matrix_A[0])
    nash_equilibria = []
    
    for i in range(m):
        for j in range(n):
            is_nash_equilibrium = True
            for k in range(m):
                if matrix_B[k][j] > matrix_B[i][j]:
                    is_nash_equilibrium = False
                    break
            for l in range(n):
                if matrix_A[i][l] > matrix_A[i][j]:
                    is_nash_equilibrium = False
                    break
            if is_nash_equilibrium:
                nash_equilibria.append((i, j))
    
    return nash_equilibria

# Example usage
matrix_A = [
    [3, 2],
    [1, 4]
]

matrix_B = [
    [2, 1],
    [3, 4]
]

nash_equilibria = find_pure_nash_equilibria(matrix_A, matrix_B)
print("Pure Nash Equilibria:")
for eq in nash_equilibria:
    print("Player 1 chooses strategy", eq[0], "and Player 2 chooses strategy", eq[1])
