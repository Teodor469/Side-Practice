def triangle_up():
    row_triangle = int(input("Enter number of rows for upwards triangle: "))

    for i in range(1, row_triangle + 1):
        for j in range(i):
            print("*", end="")
        print()

def triangle_down():
    row_triangle = int(input("Enter number of rows for downwards triangle: "))

    for i in range(row_triangle - 1, 0, - 1):
        for j in range(i):
            print("*", end="")
        print()

def rectangle():
    row_rectangle = int(input("Enter number of rows for rectangle: "))
    col_rectangle = int(input("Enter number of columns for rectangle: "))

    for i in range(row_rectangle):
        for j in range(col_rectangle):
            print("*", end="")
        print()

def pyramid():
    row_pyramid = int(input("Enter number of rows for pyramid: "))

    for i in range(row_pyramid):
        for j in range(row_pyramid - i - 1):
            print(" ", end="")

        for k in range(i * 2 + 1):
            print("*", end="")
        
        print()


while True:
    print("\nMenu: ")
    print("1. Triangle_up")
    print("2. Triangle_down")
    print("3. Rectangle")
    print("4. Pyramid")
    print("5. Exit")
    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '1':
        triangle_up()
    elif choice == '2':
        triangle_down()
    elif choice == '3':
        rectangle()
    elif choice == '4':
        pyramid()
    elif choice == '5':
        break
    else:
        print("invalid choice.")
