class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        if not self.available:
            raise ValueError("Book is already borrowed")
        self.available = False
        return False

    def return_book(self):
        if self.available:
            raise ValueError("Book is already available")
        self.available = True
        return True
    
    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return (f"{self.title} by {self.author} - {status}")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        found = self.find_book(book.title)
        if found is not None:
            raise ValueError("Book already exists")
        self.books.append(book)

    def find_book(self, title):
        for book in self.books:
            if title.lower() == book.title.lower():
                return book
        return None

    def borrow_book(self, title):
        found = self.find_book(title)
        if found is None:
            raise ValueError("Book not found")
        return found.borrow()

    def return_book(self, title):
        found = self.find_book(title)
        if found is None:
            raise ValueError("Book not found")
        return found.return_book()

    def remove_book(self, title):
        found = self.find_book(title)
        if found is None:
            raise ValueError("Book not found")
        self.books.remove(found)
        return found
    def available_books(self):
        return [book for book in self.books if book.available]






