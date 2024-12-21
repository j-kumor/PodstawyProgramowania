names = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]

longest_name = names[0]  # Start by assuming the first name is the longest

# Iterate through the list of names
for name in names:
    if len(name) > len(longest_name):  # Compare the length of current name with the longest
        longest_name = name  

print("Names:", " ".join(names))  # Join the names with spaces to print in one line
print("Longest name:", longest_name)
