#write a program to create number guessing game
import random

def number_guessing_game():
    number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    name = input("Kindly enter your name: ")
    print(f"welcome {name}!\nI have selected a number between 1 and 100. Try to guess it.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__": #it ensures that the game runs only when the script is executed directly, not when imported as a module.
    number_guessing_game()