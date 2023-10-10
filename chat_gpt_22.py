import random

random_number = random.randint(1, 100)  # Generates a random number between 1 and 100.
attempts = 5  # Maximum number of attempts allowed.
guess_attempts = 0  # Initialize the number of guess attempts.

print("Welcome to the guessing game!")
print("The machine has picked a number between 1 - 100, and you have 5 tries to guess it. Good luck.")

while guess_attempts < attempts:
    user_guess = int(input("Enter your guess here: "))
    guess_attempts += 1

    if user_guess < random_number:
        print("Too low, try again!")
    elif user_guess > random_number:
        print("Too high, try again!")
    else:
        print(f"Congratulations, you won the game! The correct number was {random_number}.")
        break
else:
    print(f"You lost the game. The correct number was {random_number}.")
