def missing_number(numbers):
    sorted_numbers = sorted(numbers)
    for i in range(1, len(sorted_numbers)):
        if sorted_numbers[i] != sorted_numbers[i-1] + 1:
            return sorted_numbers[i-1] + 1
        
numbers = [1, 2, 4, 6, 3, 7, 8]
result = missing_number(numbers)
print("Missing number:", result)