import random

random_number = random.randint(1, 100)
attempts = 5
guess_attempts = 0

print("Welcome to the Guess the Number Game!")
print(f"Guess the number between 1 and 100. You have {attempts} attempts.")

while guess_attempts < attempts:
    user_guess = int(input("Enter your guess: "))
    guess_attempts += 1
    
    if user_guess < random_number:
        print("Too low! Try again.")
    elif user_guess > random_number:
        print("Too high! Try again.")
    
    else:
        print(f"Congratulations you guessed the right number! It took you {guess_attempts} attempts")
        break
else:
    print(f"You've lost the game the correct number was {random_number}")