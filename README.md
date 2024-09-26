# Library Management System

This is a simple Library Management System written in Python using Test-Driven Development (TDD). The system allows users to:
- Add new books to the library
- Borrow books if available
- Return borrowed books
- Reserve books
- Search for books by title or author
- Check for overdue books

## Features

- **Add Books:** Users can add new books with unique identifiers (ISBN), titles, authors, and publication years.
- **Borrow Books:** Users can borrow available books. The system ensures that books are available before borrowing.
- **Return Books:** Users can return borrowed books, and the system updates the availability accordingly.
- **Reserve Books:** Users can reserve books that are currently borrowed.
- **Search Books:** Users can search for books by title or author.
- **Check Overdue Books:** The system notifies users of overdue books.

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/PushkarPattiwar/library_management_system.git
    cd library_management_system
    ```

2. (Optional) Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3. Run the tests:
    ```bash
    python -m unittest discover
    ```

## Tests

The tests are written using the `unittest` framework. All the main functionality is tested:
- Adding a book
- Registering users
- Borrowing a book
- Returning a book
- Reserving a book
- Searching for books
- Checking due dates and overdue notifications

## Usage

You can use the Library Management System by importing the classes from the `library.py` file and performing operations like adding books, registering users, borrowing, and returning books. 

