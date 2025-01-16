# Unsorted list of names
names = [
    'James',
    'Emily',
    'William',
    'Olivia',
    'Benjamin',
    'Sophia',
    'Henry'
]

# Sort the list by the length of each name using a lambda function
sorted_names = sorted(names, key=lambda name: len(name))

# Display the sorted list
print("Sorted list:")
for name in sorted_names:
    print(name)
