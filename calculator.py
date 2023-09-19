def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def devide(x, y):
    if y != 0:
        return x / y
    else:
        print("Cannot devide by zero")

while True:
    print("select operation")
    print("Operation: 1")
    print("Operation: 2")
    print("Operation: 3")
    print("Operation: 4")
    print("Operation: 5")

    choice = input("select a choice (1/2/3/4/5): ")
    if choice == '5':
        print("exiting calculator")
        break

    num1 = float(input("enter first number: "))
    num2 = float(input("enter second number: "))

    if choice == '1':
        print("result:", add(num1, num2))
    elif choice == '2':
        print("result:", subtract(num1, num2))
    elif choice == '3':
        print("result:", multiply(num1, num2))
    elif choice == '4':
        print("result:", devide(num1, num2))
    else:
        print("invalid choice")