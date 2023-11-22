input_string = input()
splitted_string = input_string.split()
opposite_number = []
for num in splitted_string:
    opposite_number.append(-int(num))

print(opposite_number)