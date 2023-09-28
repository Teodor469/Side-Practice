usr_input = input()
numbers = usr_input.split()
numbers = sum(int(num) for num in numbers)

sum_num = sum(numbers)
max_num = max(numbers)
min_num = min(numbers)
average = sum_num / len(numbers)

even_list = []
odd_list = []

for digit in numbers:
    if digit % 2 == 0:
        even_list.append(digit)
    else:
        odd_list.append(digit)

print(f"Sum of numbers: {sum_num}")
print(f"Max number: {max_num}")
print(f"Min number: {min_num}")
print(f"Average: {average}")
print(f"Even numbers: {even_list}")
print(f"Odd numbers: {odd_list}")