#write a program to create mini library system.
books = []

def add_book():
    book_id = int(input("Book ID: "))
    title = input("Title: ")
    author = input("Author: ")
    books.append({"id": book_id, "title": title, "author": author, "issued": False})

def display_books():
    for b in books:
        status = "Issued" if b["issued"] else "Available"
        print(f"{b['id']}\t{b['title']}\t{b['author']}\t{status}")

def issue_book():
    book_id = int(input("Enter Book ID to issue: "))
    for b in books:
        if b["id"] == book_id:
            if b["issued"]:
                print("Already issued.")
            else:
                b["issued"] = True
                print("Book issued.")
            return
    print("Book not found.")

def return_book():
    book_id = int(input("Enter Book ID to return: "))
    for b in books:
        if b["id"] == book_id:
            b["issued"] = False
            print("Book returned.")
            return
    print("Book not found.")

while True:
    print("\n1.Add Book 2.Display 3.Issue 4.Return 5.Exit")
    choice = int(input("Choice: "))
    if choice == 1: add_book()
    elif choice == 2: display_books()
    elif choice == 3: issue_book()
    elif choice == 4: return_book()
    elif choice == 5: break