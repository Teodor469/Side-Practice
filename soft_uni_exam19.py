def rounding(numbers):
    rounded_numbers = [round(float(num)) for num in numbers]
    return rounded_numbers

numbers = input().split()

print(rounding(numbers))