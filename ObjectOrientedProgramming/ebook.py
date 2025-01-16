# ebook.py
class Ebook:
    def __init__(self, title, author, pages):
        # Initialize the e-book with title, author, and number of pages
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 1  # Start from the first page
        self.is_open = False  # The book is initially closed

    def open_book(self):
        # Open the book to start reading
        self.is_open = True

    def close_book(self):
        # Close the book
        self.is_open = False

    def go_to_next_page(self):
        # Move to the next page if the book is open and there are more pages
        if self.is_open:
            if self.current_page < self.pages:
                self.current_page += 1
                print(f"Moved to page {self.current_page}")
            else:
                print("You are already at the last page.")
        else:
            print("The book is closed. Please open it first.")

    def go_to_previous_page(self):
        # Move to the previous page if the book is open and not at the first page
        if self.is_open:
            if self.current_page > 1:
                self.current_page -= 1
                print(f"Moved to page {self.current_page}")
            else:
                print("You are already at the first page.")
        else:
            print("The book is closed. Please open it first.")

    def display_status(self):
        # Display the current status of the book (title, author, pages, current page)
        if self.is_open:
            print(f"Reading '{self.title}' by {self.author}.")
            print(f"Total Pages: {self.pages}, Current Page: {self.current_page}")
        else:
            print(f"The book '{self.title}' by {self.author} is closed.")
