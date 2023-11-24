sequence_of_numbers = input().split()

abs_list = []

for number in sequence_of_numbers:
    abs_list.append(abs(float(sequence_of_numbers)))

print(abs_list)
