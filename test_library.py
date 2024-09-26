# test_library.py

import unittest
from library import Library, Book, BookNotAvailableError

class TestLibrary(unittest.TestCase):
    def setUp(self):
        # This method runs before every test. We'll instantiate the Library here.
        self.library = Library()

    def test_add_book(self):
        # Test adding a book to the library
        book = Book('12345', 'Clean Code', 'Robert C. Martin', 2008)
        self.library.add_book(book)
        self.assertIn(book, self.library.available_books)  # Check that the book is in the available_books list

    def test_borrow_book(self):
        # Test borrowing a book from the library
        book = Book('12345', 'Clean Code', 'Robert C. Martin', 2008)
        self.library.add_book(book)
        self.library.borrow_book('12345')
        self.assertNotIn(book, self.library.available_books)  # Ensure the book is removed from available books

    def test_borrow_non_existing_book(self):
        # Test trying to borrow a book that does not exist or is already borrowed
        with self.assertRaises(BookNotAvailableError):
            self.library.borrow_book('99999')  # ISBN 99999 does not exist in the library

    def test_return_book(self):
        # Test returning a borrowed book
        book = Book('12345', 'Clean Code', 'Robert C. Martin', 2008)
        self.library.add_book(book)
        self.library.borrow_book('12345')
        self.library.return_book('12345')
        self.assertIn(book, self.library.available_books)  # Ensure the book is returned to available books

    def test_view_available_books(self):
        # Test viewing all available books
        book1 = Book('12345', 'Clean Code', 'Robert C. Martin', 2008)
        book2 = Book('67890', 'The Pragmatic Programmer', 'Andrew Hunt', 1999)
        self.library.add_book(book1)
        self.library.add_book(book2)
        self.assertEqual(len(self.library.available_books), 2)  # We added 2 books, so 2 should be available

if __name__ == '__main__':
    unittest.main()
