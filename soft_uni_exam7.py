gifts = input()
gifts_name = gifts.split()
gifts_list = gifts_name.copy()

while True:
    command = input()
    if command == 'No Money':
        break

    command_parts = command.split()
    command_type = command_parts[0]

    if command_type == "OutOfStock":
        gift_to_remove = command_parts[1]
        for i in range(len(gifts_list)):
            if gifts_list[i] == gift_to_remove:
                gifts_list[i] = "None"
    elif command_type == "Required":
        replaced_gift = command_parts[1]
        index = int(command_parts[2])
        if 0 <= index < len(gifts_list):
            gifts_list[index] = replaced_gift
    elif command_type == "JustInCase":
        gifts_list[-1] = command_parts[1]

final_gifts = []
for gift in gifts_list:
    if gift != "None":
        final_gifts.append(gift)

print(" ".join(final_gifts))