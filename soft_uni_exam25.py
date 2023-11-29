def decode_message(message, commands):
    for command in commands:
        tokens = command.split('|')
        instructions = tokens[0]

        if instructions == 'Move':
            num_letters = int(tokens[1])
            message = message[num_letters:] + message[:num_letters]

        elif instructions == 'Insert':
            index = int(tokens[1])
            value = tokens[2]
            message_list = list(message)
            message_list.insert(index, value)
            message = ''.join(message_list)

        elif instructions == 'ChangeAll':
            substring = tokens[1]
            replacement = tokens[2]
            message = message.replace(substring, replacement)

        elif instructions == 'Decode':
            print(f"The decrypted message is: {message}")

encrypted_message = input()
commands_list = []

while True:
    command = input()
    commands_list.append(command)
    if command == 'Decode':
        break

decode_message(encrypted_message, commands_list)
