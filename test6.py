first_limit = int(input())
second_limit = int(input())
third_limit = int(input())

for first_digit in range(2, first_limit + 1, 2):
    for second_digit in range(2, second_limit + 1):
        if second_digit == 2 or second_digit == 3 or second_digit == 5 or second_digit == 7:
            for third_digit in range(2, third_limit + 1, 2):
                print(f"{first_digit} {second_digit} {third_digit}")

