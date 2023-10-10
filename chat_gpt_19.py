def remove_duplicates(input_list):
    # Your code here
    unique_list = []
    for i in input_list:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list
# Example usage:
original_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
result_list = remove_duplicates(original_list)
print(result_list)