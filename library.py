# library.py

class BookNotAvailableError(Exception):
    """Custom exception for unavailable books."""
    pass

class Book:
    """Represents a book in the library."""
    def __init__(self, isbn, title, author, publication_year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def __eq__(self, other):
        return self.isbn == other.isbn

class Library:
    """Library class manages books and borrowing/returning operations."""
    def __init__(self):
        self.available_books = []  # List of available books
        self.borrowed_books = {}   # Dictionary of borrowed books (key: ISBN, value: Book)

    def add_book(self, book):
        """Adds a book to the library's available books."""
        self.available_books.append(book)

    def borrow_book(self, isbn):
        """Allows users to borrow a book if available. Otherwise raises an error."""
        book = self.find_book(isbn, self.available_books)
        if book:
            self.available_books.remove(book)
            self.borrowed_books[isbn] = book
        else:
            raise BookNotAvailableError(f"Book with ISBN {isbn} is not available.")

    def return_book(self, isbn):
        """Allows users to return a borrowed book."""
        book = self.borrowed_books.pop(isbn, None)
        if book:
            self.available_books.append(book)

    def find_book(self, isbn, book_list):
        """Finds a book by ISBN from a given list."""
        for book in book_list:
            if book.isbn == isbn:
                return book
        return None
