import json

harry_potter = {
    "title": "Harry Potter and the Sorcerer's Stone",
    "author": "J.K. Rowling",
    "genre": "Fantasy",
    "publication_year": 1997,
    "description": "A young boy discovers he is a wizard and attends a magical school, where he faces numerous challenges and adventures, including a dark force trying to conquer the wizarding world."
}

#  Write the dictionary data
with open('favourite.json', 'w', encoding='utf-8') as file:
    json.dump(harry_potter, file, ensure_ascii=False, indent=4)

print("Data has been written to 'favourite.json'.")
