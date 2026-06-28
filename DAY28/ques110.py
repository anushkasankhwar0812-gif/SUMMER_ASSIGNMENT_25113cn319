#write a program to create menu driven array operations system
arr = []

while True:
    print("\n===== Array Operations Menu =====")
    print("1. Insert Element")
    print("2. Display Array")
    print("3. Search Element")
    print("4. Delete Element")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        element = int(input("Enter element to insert: "))
        arr.append(element)
        print("Element inserted successfully.")

    elif choice == 2:
        if len(arr) == 0:
            print("Array is empty.")
        else:
            print("Array elements are:")
            for i in arr:
                print(i, end=" ")
            print()

    elif choice == 3:
        key = int(input("Enter element to search: "))

        if key in arr:
            position = arr.index(key)
            print("Element found at index", position)
        else:
            print("Element not found.")

    elif choice == 4:
        element = int(input("Enter element to delete: "))

        if element in arr:
            arr.remove(element)
            print("Element deleted successfully.")
        else:
            print("Element not found.")

    elif choice == 5:
        print("Program terminated.")
        break

    else:
        print("Invalid choice. Please try again.")