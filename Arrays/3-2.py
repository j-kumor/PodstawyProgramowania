import random 


arr1 = [3, 7, 1, 0, 4]

arr2 = [[2, 3], [7, 1], [0, 4]]

arr3 = [7 for i in range(5)]

arr4 = [i for i in range(1, 10)]

arr5 = [i * 2 for i in range(1, 10)]

arr6 = [random.randint(1, 20) for i in range(10)]

# Tablica 2D, gdzie każdy element to pusta lista, a tablica ma 5 wierszy
arr7 = [[] for i in range(5)]

# Tablica 2D, która ma 4 wiersze, a każdy wiersz zawiera dwa elementy, które są równe 1
arr8 = [[1 for i in range(2)] for j in range(4)]

# Tablica 2D, która ma 5 wierszy i 3 kolumny, a każdy element to losowa liczba z zakresu <1, 20>
arr9 = [[random.randint(1, 20) for i in range(3)] for j in range(5)]

arr10 = [4, 0, 3]

arr11 = [0] * 15

arr12 = [random.randint(1, 30) for i in range(10)]

arr13 = [random.choice([0, 1]) for i in range(20)]

# arr14: Tablica 2D o 5 wierszach i 2 kolumnach, wypełniona wartościami False
arr14 = [[False, False] for i in range(5)]

print("arr1:", arr1)
print("arr2:", arr2)
print("arr3:", arr3)
print("arr4:", arr4)
print("arr5:", arr5)
print("arr6:", arr6)
print("arr7:", arr7)
print("arr8:", arr8)
print("arr9:", arr9)
print("arr10:", arr10)
print("arr11:", arr11)
print("arr12:", arr12)
print("arr13:", arr13)
print("arr14:", arr14)
