# We need to print the numbers from 1 to 49 in a specific format.
# The format is such that each column contains numbers starting from 1 to 7, then 8 to 14, and so on.

# Loop over each column
for i in range(7):
    # Loop over each row (7 rows total)
    for j in range(7):
        # Calculate the number by using the formula for each row and column
        print(i + 1 + j * 7, end=" ")
    # Print a newline after each row
    print()
