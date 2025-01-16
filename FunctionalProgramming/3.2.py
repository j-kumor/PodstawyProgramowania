# Input sentence
sentence = 'I completely agree with you'

# Split the sentence into words and calculate the number of letters in each word
result = list(map(lambda word: len(word), sentence.split()))

# Display the result
print(f"No. of letters in words: {result}")
