def sort_names():
    name_list = [name for name in input().split(', ')]
    return sorted(name_list, key=lambda x: (-len(x), x))

print(sort_names())