def move(input_string, num_letters):
    if num_letters < 0:
        raise ValueError("Invalid number of letters to move.")

    num_letters = min(num_letters, len(input_string))
    moved_part = input_string[:num_letters]
    rest_of_string = input_string[num_letters:]
    moved_string = rest_of_string + moved_part

    return moved_string

def insert_value(input_string, index, value):
    if index < 0 or index > len(input_string):
        raise ValueError("Invalid index.")

    inserted_string = input_string[:index] + value + input_string[index:]

    return inserted_string

def change_all(input_string, substring, replacement):
    return input_string.replace(substring, replacement)

encrypted_message = input()
instructions = []

while True:
    command = input()
    if command == "Decode":
        break
    instructions.append(command)

decrypted_message = encrypted_message

for instruction in instructions:
    command, *args = instruction.split("|")
    if command == "Move":
        num_letters = int(args[0])
        decrypted_message = move(decrypted_message, num_letters)
    elif command == "Insert":
        index = int(args[0])
        value = args[1]
        decrypted_message = insert_value(decrypted_message, index, value)
    elif command == "ChangeAll":
        substring = args[0]
        replacement = args[1]
        decrypted_message = change_all(decrypted_message, substring, replacement)

print(f"The decrypted message is: {decrypted_message}")
