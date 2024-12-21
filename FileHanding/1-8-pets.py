def read_from_file(name):
    with open(name) as file:
        content = file.read()
    return content

file_content = read_from_file('pets.txt')

print(file_content)

# Count the number of words
total_words = 0
lines = file_content.splitlines()  # Split the content into lines

for line in lines:
    words = line.split()  # Split each line into words
    total_words += len(words)  # Add the number of words in this line to the total

print('Total number of words:', total_words)