def even(numbers):
    return numbers % 2 == 0

def odd(numbers):
    return numbers % 2 == 1

def negative(numbers):
    return numbers < 0

def positive(numbers):
    return numbers >= 0

n = int(input())
numbers_list = []

for _ in range(n):
    numbers = int(input())
    numbers_list.append(numbers)

category_command = input()
filtered_list = []

if category_command == "even":
    filtered_list = [num for num in numbers_list if even(num)]
elif category_command == "odd":
    filtered_list = [num for num in numbers_list if odd(num)]
elif category_command == "negative":
    filtered_list = [num for num in numbers_list if negative(num)]
elif category_command == "positive":
    filtered_list = [num for num in numbers_list if positive(num)]

print(filtered_list)
