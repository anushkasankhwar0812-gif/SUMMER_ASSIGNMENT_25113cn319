#write a program to create quiz game application.
def quiz_game():
    print("Welcome to the Quiz Game!")
    name = input("Kindly enter your name: ")
    input(f"welcome {name}!\ntry to give correct answers to score the highest.\nGOOD LUCK!")
    score = 0

    questions = [
        ("What is the capital of France?", "Paris"),
        ("the novel harry potter is written by whom?","jk rolling"),
        ("What is 2 + 2?", "4"),
        ("What is the largest planet in our solar system?", "Jupiter"),("who is the prime minister of india:?","narendra modi"),
    ]

    for question, correct_answer in questions:
        print(f"\n{question}")
        user_answer = input("Your answer: ").strip()

        if user_answer.lower() == correct_answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer}.")

    print(f"\n{name}, your final score is: {score}/{len(questions)}")
    if score==len(questions):
        print(f"CONGRATULATIONS!{name}\nYOU WON THE GAME")
    else:
        print(f"its okay{name}!\nbetter luck next time")

if __name__ == "__main__":
    quiz_game()
