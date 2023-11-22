factor_number = int(input())
count_number = int(input())
multiples = []

for num in range(1, count_number + 1):
    multiple = factor_number * num
    multiples.append(multiple)

print(multiples)