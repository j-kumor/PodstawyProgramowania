translations = {
    'computer': 'komputer',
    'mouse': 'myszka',
    'keyboard': 'klawiatura',
    'printer': 'drukarka'
}

# Ask the user to enter a word in English
english_word = input("Enter an English word: ").lower()  # Convert input to lowercase to handle case insensitivity

# Check if the word is in the dictionary and provide the translation or a message if unavailable
if english_word in translations:
    print(f"The Polish translation of '{english_word}' is '{translations[english_word]}'.")
else:
    print(f"Sorry, the translation for '{english_word}' is unavailable.")
