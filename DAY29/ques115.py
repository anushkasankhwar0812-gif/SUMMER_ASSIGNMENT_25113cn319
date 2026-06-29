#write a program to create menu driven strings operations system
def get_string():
    return input("Enter a string: ")


def display_length(s):
    print(f"Length of string: {len(s)}")


def to_uppercase(s):
    print(f"Uppercase: {s.upper()}")


def to_lowercase(s):
    print(f"Lowercase: {s.lower()}")


def reverse_string(s):
    print(f"Reversed string: {s[::-1]}")


def is_palindrome(s):
    cleaned = s.replace(" ", "").lower()
    if cleaned == cleaned[::-1]:
        print(f'"{s}" is a palindrome.')
    else:
        print(f'"{s}" is not a palindrome.')


def count_vowels_consonants(s):
    vowels = 0
    consonants = 0
    for ch in s.lower():
        if ch.isalpha():
            if ch in 'aeiou':
                vowels += 1
            else:
                consonants += 1
    print(f"Vowels: {vowels}")
    print(f"Consonants: {consonants}")


def count_words(s):
    words = s.split()
    print(f"Word count: {len(words)}")


def find_replace(s):
    find_val = input("Enter substring to find: ")
    replace_val = input("Enter substring to replace with: ")
    result = s.replace(find_val, replace_val)
    print(f"Result: {result}")
    return result


def remove_spaces(s):
    print(f"String without spaces: {s.replace(' ', '')}")


def count_occurrences(s):
    sub = input("Enter substring to count: ")
    print(f"'{sub}' occurs {s.count(sub)} time(s).")


def concatenate_string(s):
    s2 = input("Enter another string to concatenate: ")
    result = s + s2
    print(f"Concatenated string: {result}")
    return result


def check_substring(s):
    sub = input("Enter substring to check: ")
    if sub in s:
        print(f"'{sub}' is present in the string at index {s.find(sub)}.")
    else:
        print(f"'{sub}' is not present in the string.")


def sort_characters(s):
    sorted_str = ''.join(sorted(s))
    print(f"Sorted characters: {sorted_str}")


def show_menu():
    print("\n----- STRING OPERATIONS MENU -----")
    print("1.  Enter/Update String")
    print("2.  Display Length")
    print("3.  Convert to Uppercase")
    print("4.  Convert to Lowercase")
    print("5.  Reverse String")
    print("6.  Check Palindrome")
    print("7.  Count Vowels and Consonants")
    print("8.  Count Words")
    print("9.  Find and Replace")
    print("10. Remove Spaces")
    print("11. Count Occurrences of Substring")
    print("12. Concatenate Another String")
    print("13. Check if Substring Exists")
    print("14. Sort Characters")
    print("15. Display Current String")
    print("16. Exit")
    print("-----------------------------------")


def main():
    current_string = ""

    while True:
        show_menu()
        choice = input("Enter your choice (1-16): ")

        if choice == '1':
            current_string = get_string()
        elif not current_string and choice not in ('1', '16'):
            print("No string set yet. Please choose option 1 first.")
        elif choice == '2':
            display_length(current_string)
        elif choice == '3':
            to_uppercase(current_string)
        elif choice == '4':
            to_lowercase(current_string)
        elif choice == '5':
            reverse_string(current_string)
        elif choice == '6':
            is_palindrome(current_string)
        elif choice == '7':
            count_vowels_consonants(current_string)
        elif choice == '8':
            count_words(current_string)
        elif choice == '9':
            current_string = find_replace(current_string)
        elif choice == '10':
            remove_spaces(current_string)
        elif choice == '11':
            count_occurrences(current_string)
        elif choice == '12':
            current_string = concatenate_string(current_string)
        elif choice == '13':
            check_substring(current_string)
        elif choice == '14':
            sort_characters(current_string)
        elif choice == '15':
            print(f"Current string: {current_string}")
        elif choice == '16':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 16.")


if __name__ == "__main__":
    main()