#write a program to create menu driven array operations system.
def create_array():
    n = int(input("Enter number of elements: "))
    arr = []
    for i in range(n):
        while True:
            try:
                val = float(input(f"Enter element {i + 1}: "))
                arr.append(val)
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
    return arr


def display_array(arr):
    if not arr:
        print("Array is empty.")
    else:
        print("Array:", arr)


def insert_element(arr):
    val = float(input("Enter value to insert: "))
    pos = int(input(f"Enter position (0 to {len(arr)}): "))
    if 0 <= pos <= len(arr):
        arr.insert(pos, val)
        print("Element inserted successfully.")
    else:
        print("Invalid position.")


def delete_element(arr):
    if not arr:
        print("Array is empty.")
        return
    pos = int(input(f"Enter position to delete (0 to {len(arr) - 1}): "))
    if 0 <= pos < len(arr):
        removed = arr.pop(pos)
        print(f"Removed element: {removed}")
    else:
        print("Invalid position.")


def search_element(arr):
    if not arr:
        print("Array is empty.")
        return
    val = float(input("Enter value to search: "))
    if val in arr:
        print(f"Element found at index {arr.index(val)}.")
    else:
        print("Element not found.")


def update_element(arr):
    if not arr:
        print("Array is empty.")
        return
    pos = int(input(f"Enter position to update (0 to {len(arr) - 1}): "))
    if 0 <= pos < len(arr):
        val = float(input("Enter new value: "))
        arr[pos] = val
        print("Element updated successfully.")
    else:
        print("Invalid position.")


def sort_array(arr):
    if not arr:
        print("Array is empty.")
        return
    order = input("Sort ascending or descending? (a/d): ").lower()
    arr.sort(reverse=(order == 'd')) 
    print("Array sorted successfully.")


def reverse_array(arr):
    arr.reverse()
    print("Array reversed successfully.")


def sum_array(arr):
    print(f"Sum of elements: {sum(arr)}")


def average_array(arr):
    if not arr:
        print("Array is empty.")
        return
    print(f"Average of elements: {sum(arr) / len(arr)}")


def max_min_array(arr):
    if not arr:
        print("Array is empty.")
        return
    print(f"Maximum: {max(arr)}")
    print(f"Minimum: {min(arr)}")


def show_menu():
    print("\n----- ARRAY OPERATIONS MENU -----")
    print("1.  Create Array")
    print("2.  Display Array")
    print("3.  Insert Element")
    print("4.  Delete Element")
    print("5.  Search Element")
    print("6.  Update Element")
    print("7.  Sort Array")
    print("8.  Reverse Array")
    print("9.  Sum of Elements")
    print("10. Average of Elements")
    print("11. Maximum and Minimum")
    print("12. Exit")
    print("----------------------------------")


def main():
    arr = []

    while True:
        show_menu()
        choice = input("Enter your choice (1-12): ")

        if choice == '1':
            arr = create_array()
        elif choice == '2':
            display_array(arr)
        elif choice == '3':
            insert_element(arr)
        elif choice == '4':
            delete_element(arr)
        elif choice == '5':
            search_element(arr)
        elif choice == '6':
            update_element(arr)
        elif choice == '7':
            sort_array(arr)
        elif choice == '8':
            reverse_array(arr)
        elif choice == '9':
            sum_array(arr)
        elif choice == '10':
            average_array(arr)
        elif choice == '11':
            max_min_array(arr)
        elif choice == '12':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 12.")


if __name__== "__main__":
    main()