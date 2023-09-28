command = input()
total_price = 0
total_tax = 0

while command != 'special' and command != 'regular':
    price = float(command)
    
    if price <= 0:
        print("Invalid price!")
    else:
        tax = price * 0.20
        total_price += price
        total_tax += tax
    
    command = input()

if total_price <= 0:
    print("Invalid order!")
else:
    if command == 'special':
        after_tax = total_price + total_tax
        after_tax -= after_tax * 0.10

        print("Congratulations you've just bought a new computer!")
        print(f"Price without taxes: {total_price:.2f}$")
        print(f"Taxes: {total_tax:.2f}$")
        print("-----------")
        print(f"Total price: {after_tax:.2f}$")
    else:
        print("Congratulations you've just bought a new computer!")
        print(f"Price without taxes: {total_price:.2f}$")
        print(f"Taxes: {total_tax:.2f}$")
        print("-----------")
        print(f"Total price: {total_price + total_tax:.2f}$")
