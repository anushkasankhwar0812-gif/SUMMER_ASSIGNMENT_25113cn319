#write a program to create a contact manager system
contacts = []

while True:
    print("\n===== Contact Management System =====")
    print("1. Add Contact")
    print("2. Display Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email: ")

        contact = {
            "name": name,
            "phone": phone,
            "email": email
        }

        contacts.append(contact)
        print("Contact added successfully!")

    elif choice == 2:
        if len(contacts) == 0:
            print("No contacts available.")
        else:
            print("\nContact List:")
            for contact in contacts:
                print("\nName:", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])

    elif choice == 3:
        search_name = input("Enter name to search: ")
        found = False

        for contact in contacts:
            if contact["name"].lower() == search_name.lower():
                print("\nContact Found")
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])
                found = True
                break

        if not found:
            print("Contact not found.")

    elif choice == 4:
        delete_name = input("Enter name to delete: ")
        found = False

        for contact in contacts:
            if contact["name"].lower() == delete_name.lower():
                contacts.remove(contact)
                print("Contact deleted successfully!")
                found = True
                break

        if not found:
            print("Contact not found.")

    elif choice == 5:
        print("Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")