# Personal Mini-Toolkit
# This program provides three useful tools through a simple menu.


# Tool 1: Simple Calculator
# This tool asks for two numbers and performs a selected calculation.
def calculator():
    print("\n--- Simple Calculator ---")

    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))

    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    operation = input("Enter your choice: ")

    if operation == "1":
        result = number1 + number2
        print(f"{number1} + {number2} = {result}")

    elif operation == "2":
        result = number1 - number2
        print(f"{number1} - {number2} = {result}")

    elif operation == "3":
        result = number1 * number2
        print(f"{number1} x {number2} = {result}")

    elif operation == "4":
        if number2 != 0:
            result = number1 / number2
            print(f"{number1} / {number2} = {result}")
        else:
            print("Sorry, you cannot divide by zero.")

    else:
        print("Invalid operation. Please choose 1, 2, 3, or 4.")


# Tool 2: To-Do List
# This tool allows the user to add, remove, and view tasks stored in a list.
def todo_list():
    tasks = []

    while True:
        print("\n--- To-Do List ---")
        print("1. Add task")
        print("2. Remove task")
        print("3. Show tasks")
        print("4. Back to main menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter a task: ")
            tasks.append(task)
            print(f"Task '{task}' has been added.")

        elif choice == "2":
            task = input("Enter the task to remove: ")

            if task in tasks:
                tasks.remove(task)
                print(f"Task '{task}' has been removed.")
            else:
                print("That task is not on your list.")

        elif choice == "3":
            print("\nYour To-Do List:")

            if len(tasks) == 0:
                print("Your list is empty.")
            else:
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

        elif choice == "4":
            print("Returning to the main menu...")
            break

        else:
            print("Invalid choice. Please choose 1, 2, 3, or 4.")


# Tool 3: Number Guessing Game
# This tool keeps asking for guesses until the user finds the secret number.
def guessing_game():
    secret_number = 7
    attempts = 0

    print("\n--- Number Guessing Game ---")
    print("I am thinking of a number between 1 and 20.")

    while True:
        guess = int(input("Enter your guess: "))
        attempts = attempts + 1

        if guess > secret_number:
            print("Too high!")

        elif guess < secret_number:
            print("Too low!")

        else:
            print(f"Congratulations! You guessed the number {secret_number}.")
            print(f"You got it in {attempts} tries!")
            break


# Main menu
print("========================================")
print("      WELCOME TO MY PERSONAL TOOLKIT")
print("========================================")

while True:
    print("\nPlease choose a tool:")
    print("1. Simple Calculator")
    print("2. To-Do List")
    print("3. Number Guessing Game")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        calculator()

    elif choice == "2":
        todo_list()

    elif choice == "3":
        guessing_game()

    elif choice == "4":
        print("\nThank you for using my Personal Mini-Toolkit!")
        print("Goodbye!")
        break

    else:
        print("\nSorry, that choice is not on the menu. Please try again.")
