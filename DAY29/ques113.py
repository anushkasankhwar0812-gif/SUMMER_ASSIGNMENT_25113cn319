#write a program to create menu driven calculator

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b


def modulus(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a % b


def power(a, b):
    return a ** b


def show_menu():
    print("\n----- MENU DRIVEN CALCULATOR -----")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Power (**)")
    print("7. Exit")
    print("-----------------------------------")


def get_numbers():
    while True:
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            return a, b
        except ValueError:
            print("Invalid input. Please enter numeric values.")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-7): ")

        if choice == '7':
            print("Exiting calculator. Goodbye!")
            break

        if choice not in ('1', '2', '3', '4', '5', '6'):
            print("Invalid choice. Please select a number between 1 and 7.")
            continue

        a, b = get_numbers()

        if choice == '1':
            print(f"Result: {a} + {b} = {add(a, b)}")
        elif choice == '2':
            print(f"Result: {a} - {b} = {subtract(a, b)}")
        elif choice == '3':
            print(f"Result: {a} * {b} = {multiply(a, b)}")
        elif choice == '4':
            print(f"Result: {a} / {b} = {divide(a, b)}")
        elif choice == '5':
            print(f"Result: {a} % {b} = {modulus(a, b)}")
        elif choice == '6':
            print(f"Result: {a} ** {b} = {power(a, b)}")

        again = input("\nDo you want to perform another calculation? (y/n): ")
        if again.lower() != 'y':
            print("Exiting calculator. Goodbye!")
            break


if __name__ == "__main__":
    main()