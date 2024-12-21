# 3x3 Tic-Tac-Toe board
tic_tac_toe_board = [
   ['X', 'O', 'X'],
   [' ', 'X', 'O'],
   ['O', ' ', 'X']
]

# Loop through each row of the board
for row in tic_tac_toe_board:
   # Loop through each element in the row
   for element in row:
      print(element, end=" ")  # Print element and stay on the same line
   print()  # Move to the next line after each row
