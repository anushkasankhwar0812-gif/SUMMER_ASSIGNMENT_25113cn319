#write a program to create voting eligibility system
def voting_eligibility_system():
    print("Welcome to the Voting Eligibility System!")
    name = input("Kindly enter your name: ")
    try:
        age = int(input(f"Hello {name}, please enter your age: "))

        if age < 0:
            print("Age cannot be negative. Please enter a valid age.")
        elif age < 18:
            print(f"Sorry {name}, you are not eligible to vote. You need to be at least 18 years old.")
        else:
            print(f"Congratulations {name}, you are eligible to vote!")

    except ValueError:
        print("Please enter a valid integer for age.")

if __name__ == "__main__":
    voting_eligibility_system()