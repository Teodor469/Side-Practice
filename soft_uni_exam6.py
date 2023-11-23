list_of_string_numbers = input().split()
list_of_integer_numbers = [int(x) for x in list_of_string_numbers]

count_of_numbers_to_remove = int(input())

for _ in range(count_of_numbers_to_remove):
    if list_of_integer_numbers:
        smallest = min(list_of_integer_numbers)
        list_of_integer_numbers.remove(smallest)

print(', '.join(map(str, list_of_integer_numbers)))