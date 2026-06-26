#write a program to create ATM STIMULATION
def atm_simulation():
    print("Welcome to the ATM Simulation!")
    name = input("Kindly enter your name: ")
    balance = 1000  # Initial balance

    while True:
        print("\nPlease choose an option:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            print(f"{name}, your current balance is: ${balance:.2f}")
        elif choice == '2':
            try:
                deposit_amount = float(input("Enter the amount to deposit: "))
                if deposit_amount <= 0:
                    print("Deposit amount must be positive.")
                else:
                    balance += deposit_amount
                    print(f"Successfully deposited ${deposit_amount:.2f}. New balance: ${balance:.2f}")
            except ValueError:
                print("Please enter a valid number for the deposit amount.")
        elif choice == '3':
            try:
                withdraw_amount = float(input("Enter the amount to withdraw: "))
                if withdraw_amount <= 0:
                    print("Withdrawal amount must be positive.")
                elif withdraw_amount > balance:
                    print("Insufficient funds for this withdrawal.")
                else:
                    balance -= withdraw_amount
                    print(f"Successfully withdrew ${withdraw_amount:.2f}. New balance: ${balance:.2f}")
            except ValueError:
                print("Please enter a valid number for the withdrawal amount.")
        elif choice == '4':
            print(f"Thank you for using the ATM Simulation, {name}! Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    atm_simulation()
