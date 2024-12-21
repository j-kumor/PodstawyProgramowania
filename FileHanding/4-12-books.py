import csv  # Import the csv module to handle CSV file operations

FILEPATH = 'books.csv'

def read_books(file_path):
    """Read books from a CSV file and return a list of dictionaries."""
    books = []  # Initialize an empty list to store book data
    with open(file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)  # Create a CSV DictReader object
        for row in reader:
            books.append(row)
    return books

def extract_unique_genre(books):
    # Create a set of unique genres by iterating through the books
    return set([b['Genre'] for b in books])

def filter_books_by_genre(books, genre):
    # Return a list of books that match the specified genre
    return [book for book in books if book['Genre'] == genre]

def save_books_to_file(books, genre):
    # Format the genre for the filename
    genre_lowercased = genre.lower().replace(' ', '-')
    file_path = f'books_{genre_lowercased}.txt'  # Create the output file path
    # Open the output file for writing
    with open(file_path, 'w', encoding='utf-8') as file:
        # Write each book's details to the file
        for book in books:
            file.write(f"{book['Title']}, {book['Author']}, {book['Genre']}, {book['Year']}\n")
    return file_path  # Return the path of the saved file

def process_genre(books, genre):
    genre_books = filter_books_by_genre(books, genre)
    file_path = save_books_to_file(genre_books, genre)
    print(f"Saved {len(genre_books)} books to {file_path}")

def main():
    books = read_books(FILEPATH)
    genre = extract_unique_genre(books)

    # Process each unique genre
    for g in genre:
        process_genre(books, g)  # Filter and save books for each genre


if __name__ == "__main__":
    main() 