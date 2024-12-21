import random 


def rand_elem(array):
    return random.choice(array)  

arr = [10, 20, 30, 40, 50]

print("Randomly selected elements:")
for _ in range(5):  # Select 5 random elements and print them
    print(rand_elem(arr))
