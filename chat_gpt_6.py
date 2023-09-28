numbers = []

while True:
    user_input = input()

    if user_input == "":
        break
    number = int(user_input)
    numbers.append(number)

even_total = 0
for num in numbers:
    if num % 2 == 0:
        even_total += num
    
print(even_total)