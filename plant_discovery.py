class PlantCollection:
    def __init__(self) -> None:
        self.plants = {}

    def rate_plant(self, plant, rating):
        if plant in self.plants:
            self.plants[plant]['ratings'].append(int(rating))
        else:
            print("error")

    def update_rarity(self, plant, new_rarity):
        if plant in self.plants:
            self.plants[plant]['rarity'] = int(new_rarity)
        else:
            print("error")

    def reset(self, plant):
        if plant in self.plants:
            self.plants[plant]['ratings'] = []
        else:
            print("error")

    def exhibition(self):
        print("Plants for the exhibition:")
        for plant, data in self.plants.items():
            rarity = data['rarity']
            ratings = data['ratings']
            average_rating = sum(ratings) / len(ratings) if ratings else 0
            print(f"- {plant}; Rarity: {rarity}; Rating: {average_rating:.2f}")


plants = PlantCollection()
n = int(input())
commands = []

for _ in range(n):
    plant_info = input().split('<->')
    plant_name, rarity = plant_info[0], int(plant_info[1])
    plants.plants[plant_name] = {'rarity': rarity, 'ratings': []}

while True:
    command = input().split()
    action = command[0]

    if action == 'Exhibition':
        break
    else:
        commands.append(command)

for command in commands:
    action = command[0]

    if action == 'Rate:':
        plants.rate_plant(command[1], command[3])
    elif action == 'Update:':
        plants.update_rarity(command[1], command[3])
    elif action == 'Reset:':
        plants.reset(command[1])

plants.exhibition()
