def transpose_matrix(m):
    # Transpose the matrix using list comprehension
    return [list(row) for row in zip(*m)]

# First matrix
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Second matrix
matrix2 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 0]
]

# Third matrix
matrix3 = [
    [5, 6, 7, 8]
]

# Function to print the matrix in a readable way
def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

# Transpose and print the matrices
print("Transposed matrix 1:")
print_matrix(transpose_matrix(matrix1))

print("\nTransposed matrix 2:")
print_matrix(transpose_matrix(matrix2))

print("\nTransposed matrix 3:")
print_matrix(transpose_matrix(matrix3))
