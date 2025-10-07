# Project 6: Mini Library Management System 

library = {
    "python101": "Available",
    "datascience": "Available",
    "algorithms": "Available"
}

borrowed_books = set()

while True:
    print("\n--- Library Menu ---")
    print("1 - Add Book")
    print("2 - Borrow Book")
    print("3 - Return Book")
    print("4 - View All Books")
    print("5 - Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        book = input("Enter book name: ").lower()
        if book in library:
            print("This book already exists.")
        else:
            library[book] = "Available"
            print("Book added successfully.")

    elif choice == "2":
        book = input("Enter book name to borrow: ").lower()
        if book in library and library[book] == "Available":
            library[book] = "Borrowed"
            borrowed_books.add(book)
            print("Book borrowed successfully.")
        else:
            print("Book not available or doesn't exist.")

    elif choice == "3":
        book = input("Enter book name to return: ").lower()
        if book in borrowed_books:
            library[book] = "Available"
            borrowed_books.remove(book)
            print("Book returned successfully.")
        else:
            print("This book was not borrowed.")

    elif choice == "4":
        print("\nAll books in library:")
        for b, status in library.items():
            print(f"{b.title()} - {status}")
        print("Total books:", len(library))
        print("Borrowed books:", len(borrowed_books))

    elif choice == "5":
        print("Exiting library system. Goodbye!")
        break

    else:
        print("Invalid option. Try again.")
