stops = input()
command = input().split(":")
while command[0] != "Travel":
    if command[0] == "Add Stop":
        # Handle Add Stop command
        index, stop = int(command[1]), command[2]
        if index in range(len(stops)):
            stops = stops[:index] + stop + stops[index:]
    
    elif command[0] == "Remove Stop":
        # Handle Remove Stop command
        start_index, end_index = int(command[1]), int(command[2])
        if start_index in range(len(stops)) and end_index in range(len(stops)):
            stops = stops[:start_index] + stops[end_index +1:]
    
    elif command[0] == "Switch":
        # Handle Switch command
        old_string, new_string = command[1], command[2]
        if old_string in stops:
            stops = stops.replace(old_string, new_string)
    
    command = input().split(":")

print(f"Ready for world tour! Planned stops: {stops}")
