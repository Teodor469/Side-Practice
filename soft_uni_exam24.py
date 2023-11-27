input_names = input().split(", ")

# Sort by length in descending order
input_names.sort(key=len)

# Sort alphabetically for names with the same length
input_names.sort()

print(input_names)
