class Car:
    def __init__(self, name, mileage, fuel):
        self.name = name
        self.mileage = mileage
        self.fuel = fuel

    def drive(self, distance, fuel_needed):
        if self.fuel < fuel_needed:
            print("Not enough fuel to make that ride")
        else:
            self.mileage += distance
            self.fuel -= fuel_needed
            print(f"{self.name} driven for {distance} kilometers. {fuel_needed} liters of fuel consumed.")
            if self.mileage >= 100000:
                print(f"Time to sell the {self.name}!")
                del cars[self.name]

    def refuel(self, fuel_added):
        if self.fuel + fuel_added > 75:
            fuel_added = 75 - self.fuel
        self.fuel += fuel_added
        print(f"{self.name} refueled with {fuel_added} liters")

    def revert(self, kilometers):
        if self.mileage - kilometers < 10000:
            self.mileage = 10000
        else:
            self.mileage -= kilometers
            print(f"{self.name} mileage decreased by {kilometers} kilometers")

# Main program
cars = {}
n = int(input())

for _ in range(n):
    car_info = input().split("|")
    name, mileage, fuel = car_info[0], int(car_info[1]), int(car_info[2])
    cars[name] = Car(name, mileage, fuel)

command = input()
while command != "Stop":
    action, car_name, *params = command.split(" : ")

    if action == "Drive":
        distance, fuel_needed = map(int, params)
        cars[car_name].drive(distance, fuel_needed)
    elif action == "Refuel":
        fuel_added = int(params[0])
        cars[car_name].refuel(fuel_added)
    elif action == "Revert":
        kilometers = int(params[0])
        cars[car_name].revert(kilometers)

    command = input()

# Print the final status of all cars
for car in cars.values():
    print(f"{car.name} -> Mileage: {car.mileage} kms, Fuel in the tank: {car.fuel} lt.")
