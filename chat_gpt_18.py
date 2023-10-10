def are_consecutive(numbers):
    sorted_numbers = sorted(numbers)

    for i in range(1, len(sorted_numbers)):
        if sorted_numbers[i] != sorted_numbers[i - 1] + 1:
            return False
    return True

usr_input = input("Enter a list of numbers separated by spaces: ")
list_input = usr_input.split()
list_input = list(map(int, list_input))

if are_consecutive(list_input):
    print("The numbers are consecutive.")
else:
    print("The numbers are not consecutive.")
