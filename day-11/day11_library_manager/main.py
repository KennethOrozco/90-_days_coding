from library import Book, Library

library = Library()

library.add_book(Book("1984", "George Orwell"))
library.add_book(Book("Dune", "Frank Herbert"))
library.add_book(Book("The Hobbit", "J.R.R. Tolkien"))

while True:
    options= {
        1: "View All Books",
        2: "Add Book",
        3: "Borrow Book",
        4: "Return Book",
        5: "Remove Book",
        6: "View Available Books",
        7: "Exit"
    }
    for key, value in options.items():
        print(f"{key}. {value}")
    option = input("option: ")
    if option == "1":
        for book in library.books:
            status = "Available" if book.available else "Borrowed" 
            print(f"Title: {book.title} -- Author: {book.author} -- Status: {status}")
    elif option == "2":
        while True:
            title = input("Title: ")
            if title.strip():
                break
            print("Type a book title!")
        while True:
            author = input("Author: ")
            if author.strip():
                break
            print("Type an author!")
        try:
            library.add_book(Book(title, author))
        except ValueError as error:
            print(error)
        else:
            print("Book was added")
    elif option == "3":
        while True:
            title = input("Title: ")
            if title.strip():
                break
            print("Type a book title!")
        try:
            library.borrow_book(title)
        except ValueError as error:
            print(error)
        else:
            print("Status changed to Borrowed")
    elif option == "4":
        while True:
            title = input("Title: ")
            if title.strip():
                break
            print("Type a book title!")
        try:
            library.return_book(title)
        except ValueError as error:
            print(error)
        else:
            print("Status changed to Available")
    elif option == "5":
        while True:
            title = input("Title: ")
            if title.strip():
                break
            print("Type a book title!")
        try:
            library.remove_book(title)
        except ValueError as error:
            print(error)
        else:
            print("Book has been removed")
    elif option == "6":
        for book in library.available_books():
            print(f"{book.title} - {book.author}")
    elif option == "7":
        break
    else:
        print("Invalid option!")
                
