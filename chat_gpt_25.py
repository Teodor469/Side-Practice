plant_data = []

def add_plant():
    plant_info = input().split('<->')
    plant_name, rarity = plant_info[0], int(plant_info[1])
    plant_data.append({'name': plant_name, 'rarity': rarity})


def reset(plant_name):
    global plant_data  # Allow the function to modify the global variable
    plant_data = [plant for plant in plant_data if plant['name'] != plant_name]


def report():
    return plant_data


while True:
    command = input()
    if command == 'Report':
        print(plant_data)
        break

    if command == 'Add plant':
        add_plant()
        print(plant_data)

    if command.startswith('Reset'):
        plant_name = command.split()[-1]
        reset(plant_name)
        print(plant_data)

print("You did something wrong!")