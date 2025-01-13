paragraph = "cat dog mouse cat rat cat mouse"

# Split the paragraph into words
words = paragraph.split()

# Initialize an empty dictionary to store the word counts
word_count = {}

# Loop through each word in the list
for word in words:
    if word in word_count:
        # If it exists, increase the count by 1
        word_count[word] += 1
    else:
        # If it's not in the dictionary, add it with count 1
        word_count[word] = 1

for word, count in word_count.items():
    print(f"'{word}' appears {count} times.")
