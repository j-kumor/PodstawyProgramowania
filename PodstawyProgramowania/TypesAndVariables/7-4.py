import math

#aprawdza czy drzewo mozna sciac po obwodzie

circumference = float(input('Enter tree circumference in cm: '))

diameter = circumference / math.pi #obliczanie srednicy

tree_can_be_cut = diameter >= 50 #sprawdzanie czy jest min 50

print(f'Tree can be cut down: {tree_can_be_cut}')