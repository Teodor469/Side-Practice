my_list = [1, 2, 2, 3, 4, 4, 5]

duplicates = []

for items in my_list:
    if my_list.count(items) > 1:
        duplicates.append(items)

print(duplicates)