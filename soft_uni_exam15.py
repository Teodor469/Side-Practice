def add(operator, num1, num2):
    if operator == 'add':
        return num1 + num2
    
def subtract(operator, num1, num2):
    if operator == 'subtract':
        return num1 - num2
    
def multiply(operator, num1, num2):
    if operator == 'multiply':
        return num1 * num2
    
def divide(operator, num1, num2):
    if operator == 'divide':
        if num2 != 0:
            return num1 // num2
        return False

input_operator = input()
first_num = int(input())
second_num = int(input())

if input_operator == 'add':
    print(add(input_operator, first_num, second_num))
elif input_operator == 'subtract':
    print(subtract(input_operator, first_num, second_num))
elif input_operator == 'multiply':
    print(multiply(input_operator, first_num, second_num))
elif input_operator == 'divide':
    result = divide(input_operator, first_num, second_num)
    if result is not False:
        print(result)
    else:
        print("Error: Cannot divide by zero")
