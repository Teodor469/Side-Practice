import random

rock = "Rock"
paper = "Paper"
scissors = "Scissors"

while True:
    print('Rock')
    print("Paper")
    print("Scissors")
    print("Exit")
    choice = input('Enter your choice Rock/Paper/Scissors/Exit: ')

    if choice == 'Exit':
        break
    elif choice not in ['Rock', 'Paper', 'Scissors']:
        print("That's invalid input.")
        continue

    computer_random_number = random.randint(1, 3)
    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    else:
        computer_move = scissors

    print(f"Computer chooses {computer_move}")

    if choice == 'Rock' and computer_move == 'Scissors' or \
       choice == 'Paper' and computer_move == 'Rock' or \
       choice == 'Scissors' and computer_move == 'Paper':
        print("You win!")
    elif choice == computer_move:
        print("Draw!")
    else:
        print("You lose!")
