library_books = ["Python Basics", "Data Structures", "Operating Systems"]

def add_book():
    book = input("Enter book title to add: ")
    library_books.append(book)
    print(f"'{book}' added successfully!")

def remove_book():
    book = input("Enter book title to remove: ")
    if book in library_books:
        library_books.remove(book)
        print(f"'{book}' removed successfully!")
    else:
        print("Book not found.")

def search_book():
    book = input("Enter book title to search: ")
    if book in library_books:
        print(f"'{book}' is available in the library.")
    else:
        print("Book out of stock / not found.")

def display_books():
    print("\n--- Library Collection ---")
    for b in library_books:
        print(f"- {b}")

while True:
    print("\n1. Add Book\n2. Remove Book\n3. Search Book\n4. Display Books\n5. Exit")
    choice = input("Enter choice (1-5): ")
    if choice == '1': add_book()
    elif choice == '2': remove_book()
    elif choice == '3': search_book()
    elif choice == '4': display_books()
    elif choice == '5': break
    else: print("Invalid choice!")