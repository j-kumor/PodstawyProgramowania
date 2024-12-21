matrix = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]


for i in range(len(matrix)):
    matrix[i][i] = 1  # Set matrix[i][i] to 1 (main diagonal elements)


for row in matrix:
    print(" ".join(map(str, row)))  # Join elements of each row into a string and print
