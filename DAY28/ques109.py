#write a program to create library management system
books = []

while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        book = {
            "id": book_id,
            "title": title,
            "author": author,
            "issued": False
        }

        books.append(book)
        print("Book added successfully!")

    elif choice == 2:
        if len(books) == 0:
            print("No books available.")
        else:
            print("\nBook List:")
            for book in books:
                print("\nBook ID:", book["id"])
                print("Title:", book["title"])
                print("Author:", book["author"])
                print("Status:", "Issued" if book["issued"] else "Available")

    elif choice == 3:
        search_id = input("Enter Book ID to search: ")

        found = False
        for book in books:
            if book["id"] == search_id:
                print("\nBook Found")
                print("Title:", book["title"])
                print("Author:", book["author"])
                print("Status:", "Issued" if book["issued"] else "Available")
                found = True
                break

        if not found:
            print("Book not found.")

    elif choice == 4:
        issue_id = input("Enter Book ID to issue: ")

        found = False
        for book in books:
            if book["id"] == issue_id:
                if not book["issued"]:
                    book["issued"] = True
                    print("Book issued successfully!")
                else:
                    print("Book is already issued.")
                found = True
                break

        if not found:
            print("Book not found.")

    elif choice == 5:
        return_id = input("Enter Book ID to return: ")

        found = False
        for book in books:
            if book["id"] == return_id:
                if book["issued"]:
                    book["issued"] = False
                    print("Book returned successfully!")
                else:
                    print("Book was not issued.")
                found = True
                break

        if not found:
            print("Book not found.")

    elif choice == 6:
        print("Thank you!")
        break

    else:
        print("Invalid choice!")