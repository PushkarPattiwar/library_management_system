from datetime import datetime, timedelta

class Book:
    def __init__(self, isbn, title, author, publication_year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publication_year = publication_year

class User:
    def __init__(self, username):
        self.username = username

class BorrowedBook:
    def __init__(self, book, borrower, due_date):
        self.book = book
        self.borrower = borrower
        self.due_date = due_date

class BookNotAvailableError(Exception):
    pass

class Library:
    def __init__(self):
        self.available_books = []
        self.borrowed_books = {}
        self.reserved_books = {}
        self.users = {}

    def add_book(self, book):
        """Add a new book to the library."""
        self.available_books.append(book)

    def register_user(self, username):
        """Register a new user."""
        if username not in self.users:
            self.users[username] = User(username)
            print(f"User '{username}' registered successfully.")

    def borrow_book(self, isbn, username):
        """Borrow a book from the library."""
        if username not in self.users:
            raise ValueError(f"User '{username}' is not registered.")

        book_to_borrow = next((book for book in self.available_books if book.isbn == isbn), None)
        
        if book_to_borrow is None:
            raise BookNotAvailableError(f"Book with ISBN {isbn} is not available.")

        self.available_books.remove(book_to_borrow)
        due_date = datetime.now() + timedelta(days=14)  # Due date is 2 weeks from now
        self.borrowed_books[isbn] = BorrowedBook(book_to_borrow, username, due_date)

    def return_book(self, isbn):
        """Return a borrowed book to the library."""
        borrowed_book = self.borrowed_books.pop(isbn, None)
        if borrowed_book:
            self.available_books.append(borrowed_book.book)
        else:
            print(f"No borrowed book found with ISBN {isbn}.")

    def reserve_book(self, isbn, username):
        """Reserve a book for a user."""
        if username not in self.users:
            raise ValueError(f"User '{username}' is not registered.")

        if isbn in self.borrowed_books:
            if isbn in self.reserved_books:
                self.reserved_books[isbn].append(username)
            else:
                self.reserved_books[isbn] = [username]
        else:
            raise ValueError(f"Book with ISBN {isbn} is not borrowed.")

    def search_books(self, search_term):
        """Search for books by title or author."""
        return [book for book in self.available_books if search_term.lower() in book.title.lower() or search_term.lower() in book.author.lower()]

    def check_due_dates(self):
        """Check due dates for borrowed books and notify users."""
        for isbn, borrowed in self.borrowed_books.items():
            if borrowed.due_date < datetime.now():
                print(f"Book '{borrowed.book.title}' is overdue. Please return it.")

# Example Usage (This should be commented out in the final library.py file)
if __name__ == "__main__":
    library = Library()
    # Add books, register users, and perform operations here for manual testing.
