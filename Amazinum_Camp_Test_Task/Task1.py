import numpy as np

# Step 1: forward elimination
def forward_elimination(augmented_matrix, n):
    for i in range(n):
        # Check for zero diagonal elements
        if augmented_matrix[i][i] == 0.0:
            # Attempt row swap
            for k in range(i + 1, n):
                if augmented_matrix[k][i] != 0.0:
                    augmented_matrix[[i, k]] = augmented_matrix[[k, i]]
                    break
            else:
                return None  # No suitable row found, matrix is singular
        # Eliminate lower triangular elements
        for j in range(i+1, n):
            scaling_factor = augmented_matrix[j][i] / augmented_matrix[i][i]
            augmented_matrix[j] -= scaling_factor * augmented_matrix[i]
    return augmented_matrix

# Step 2: backward substitution
def backward_substitution(augmented_matrix, n):
    x = np.zeros(n)  # Initialize solution array with zeros
    for i in range(n-1, -1, -1):
        x[i] = augmented_matrix[i][-1]
        # Back-substitute previously found solutions
        for j in range(i+1, n):
            x[i] -= augmented_matrix[i][j] * x[j]
        x[i] /= augmented_matrix[i][i]
    return x

# Main function for the Gaussian Elimination algorithm
def gauss(a_matrix=None, b_matrix=None):
    # User input if matrices are not provided
    if a_matrix is None or b_matrix is None:
        n = int(input("Enter the number of variables: "))
        a_matrix = np.zeros((n, n), dtype=float)
        b_matrix = np.zeros((n, 1), dtype=float)
        print("Enter the elements of the A matrix, one row at a time:")
        for i in range(n):
            row = list(map(float, input().split()))
            a_matrix[i, :] = row
        print("Enter the elements of the B matrix, one element at a time:")
        for i in range(n):
            b_matrix[i, 0] = float(input())
    else:
        n = a_matrix.shape[0]

    # Check matrix dimensions
    if a_matrix.shape[0] != a_matrix.shape[1]:
        print("Not a square matrix!")
        return
    if b_matrix.shape[1] > 1 or b_matrix.shape[0] != a_matrix.shape[0]:
        print("Incorrect constant vector!")
        return

    # Create augmented matrix
    augmented_matrix = np.hstack((a_matrix.copy(), b_matrix.copy()))  # Using copies to keep original matrices intact
    print(f'Initial augmented matrix is: \n {augmented_matrix}')

    # Perform forward elimination
    upper_triangular_mat = forward_elimination(augmented_matrix, n)
    # Check if matrix singularity
    if upper_triangular_mat is None:
        print("Matrix is singular!")
        return
    print(f'Upper triangular matrix:\n{upper_triangular_mat}')

    # Perform backward substitution
    x = backward_substitution(upper_triangular_mat, n)
    return x

# Task input
variable_matrix = np.array([[1,2,3], [0,1,2], [2,0,0]], dtype=float)
constant_vector = np.array([[1], [1], [0]], dtype=float)
result1 = gauss(variable_matrix, constant_vector)
print(f'Answer for given task is: {result1}')

# User input
result2 = gauss()
print(f'Answer for user input is: {result2}')