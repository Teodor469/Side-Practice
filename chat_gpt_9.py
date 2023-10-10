user_input = int(input())
list_of_numbers = []
while True:
    if user_input <= 0:
        break
    else:
        list_of_numbers.append(user_input)
    total = sum(list_of_numbers)
    lenght = len(list_of_numbers)
    average = total / lenght
    user_input = int(input())

print(total)
print(average)