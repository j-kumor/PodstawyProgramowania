# main.py
from ebook import Ebook

def main():
    # Create an Ebook object
    my_ebook = Ebook("Python Programming", "John Doe", 200)

    # Open the book
    my_ebook.open_book()
    my_ebook.display_status()

    # Read a few pages (move to the next page)
    my_ebook.go_to_next_page()
    my_ebook.go_to_next_page()
    my_ebook.display_status()

    # Go back to the previous page
    my_ebook.go_to_previous_page()
    my_ebook.display_status()

    # Close the book
    my_ebook.close_book()
    my_ebook.display_status()

    # Try to read a page while the book is closed
    my_ebook.go_to_next_page()

if __name__ == "__main__":
    main()
