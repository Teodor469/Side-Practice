List_1 = [1, 2, 3, 4, 5]
List_2 = [3, 4, 5, 6, 7]

common = []

for item in List_1:
    if item in List_2:
        common.append(item)

print("Common Elements:", common)
