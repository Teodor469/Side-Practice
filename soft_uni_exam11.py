n = int(input())
word = input()

string_list = []

for _ in range(n):
    input_string = input()
    string_list.append(input_string)
print(string_list)

filtered_strings = []
for current_string in string_list:
    if word in string_list:
        filtered_strings.append(current_string)
print(current_string)