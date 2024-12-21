# Function to create an identity matrix of size n
def identity_matrix(n):
    # Create an n x n matrix where the diagonal elements are 1, and others are 0
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

# Function to print a 2D array in rows and columns
def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

# Create and print identity matrices of size 3, 5, and 8
print("Identity matrix of size 3:")
matrix_3 = identity_matrix(3)
print_matrix(matrix_3)

print("\nIdentity matrix of size 5:")
matrix_5 = identity_matrix(5)
print_matrix(matrix_5)

print("\nIdentity matrix of size 8:")
matrix_8 = identity_matrix(8)
print_matrix(matrix_8)