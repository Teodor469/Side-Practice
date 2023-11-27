input_string = input()

filtered_string = [letters for letters in input_string if letters.lower() not in ['a', 'o', 'u', 'e', 'i']]

print("".join(filtered_string))