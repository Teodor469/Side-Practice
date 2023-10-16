# Initialize a dictionary to store plant information
plants = {}

# Read the number of plants
n = int(input())

# Input plant information and store it in the dictionary
for _ in range(n):
    plant_info = input().split('<->')
    plant_name, rarity = plant_info[0], int(plant_info[1])
    plants[plant_name] = {'rarity': rarity, 'ratings': []}

# Process commands
while True:
    command = input()
    if command == "Exhibition":
        break
    tokens = command.split(' ')
    main_command = tokens[0]
    plant_name = tokens[1]
    if main_command == "Rate:":
        _, rating = tokens[2].split(" - ")
        if plant_name in plants:
            plants[plant_name]['ratings'].append(int(rating))
        else:
            print("error")
    elif main_command == "Update:":
        _, new_rarity = tokens[2].split(" - ")
        if plant_name in plants:
            plants[plant_name]['rarity'] = int(new_rarity)
        else:
            print("error")
    elif main_command == "Reset:":
        if plant_name in plants:
            plants[plant_name]['ratings'] = []
        else:
            print("error")

# Calculate average ratings and print the exhibition information
print("Plants for the exhibition:")
for plant_name, info in plants.items():
    rarity = info['rarity']
    ratings = info['ratings']
    average_rating = 0 if not ratings else sum(ratings) / len(ratings)
    print(f"- {plant_name}; Rarity: {rarity}; Rating: {average_rating:.2f}")
