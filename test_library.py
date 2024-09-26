import unittest
import HtmlTestRunner  
from datetime import datetime, timedelta
from library import Library, Book, User, BorrowedBook, BookNotAvailableError

class TestLibraryManagementSystem(unittest.TestCase):

    def setUp(self):
        """Set up a fresh library for each test."""
        self.library = Library()
        self.book1 = Book(isbn='12345', title='Clean Code', author='Robert C. Martin', publication_year=2008)
        self.book2 = Book(isbn='67890', title='The Pragmatic Programmer', author='Andrew Hunt', publication_year=1999)
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        self.library.register_user('bob')  # Registering bob in setup
        self.library.register_user('alice')  # Registering alice in setup

    def test_add_book(self):
        """Test adding a book to the library."""
        self.assertIn(self.book1, self.library.available_books)

    def test_register_user(self):
        """Test registering a new user."""
        self.library.register_user('charlie')
        self.assertIn('charlie', self.library.users)

    def test_borrow_book(self):
        """Test borrowing a book."""
        self.library.borrow_book('12345', 'bob')
        self.assertNotIn(self.book1, self.library.available_books)
        self.assertIn('12345', self.library.borrowed_books)

    def test_borrow_unavailable_book(self):
        """Test borrowing a book that is already borrowed."""
        self.library.borrow_book('12345', 'bob')
        with self.assertRaises(BookNotAvailableError):
            self.library.borrow_book('12345', 'alice')

    def test_return_book(self):
        """Test returning a borrowed book."""
        self.library.borrow_book('12345', 'bob')
        self.library.return_book('12345')
        self.assertIn(self.book1, self.library.available_books)

    def test_reserve_book(self):
        """Test reserving a book."""
        self.library.borrow_book('12345', 'bob')  # Borrow the book first
        self.library.reserve_book('12345', 'alice')  # Now Alice reserves it
        self.assertIn('alice', self.library.reserved_books['12345'])  # Check that Alice's reservation is recorded

    def test_search_books(self):
        """Test searching for books."""
        results = self.library.search_books('Clean')
        self.assertEqual(len(results), 1)
        self.assertIn(self.book1, results)

    def test_due_dates(self):
        """Test due date for borrowed books."""
        self.library.borrow_book('12345', 'bob')
        borrowed = self.library.borrowed_books['12345']
        self.assertIsInstance(borrowed, BorrowedBook)
        self.assertEqual(borrowed.due_date.date(), (datetime.now() + timedelta(days=14)).date())

    def test_overdue_notification(self):
        """Test overdue book notification."""
        self.library.borrow_book('12345', 'bob')
        
        # Simulate passage of time by modifying the due date directly for testing
        self.library.borrowed_books['12345'].due_date = datetime.now() - timedelta(days=1)

        # Capture printed output using a context manager
        from contextlib import redirect_stdout
        from io import StringIO
        f = StringIO()
        with redirect_stdout(f):
            self.library.check_due_dates()
        output = f.getvalue().strip()
        
        self.assertIn("Book 'Clean Code' is overdue. Please return it.", output)

if __name__ == '__main__':
    #unittest.main()
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='test-reports'))
