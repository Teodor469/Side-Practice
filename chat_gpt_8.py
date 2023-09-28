numbers = []

for i in range(5):
    num = int(input())
    numbers.append(num)

even_sum = 0

for digit in numbers:
    if digit % 2 == 0:
        even_sum += digit

print(even_sum)