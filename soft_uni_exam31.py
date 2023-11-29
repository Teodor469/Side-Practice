stock = {}

while True:
    command = input()
    if command == "statistics":
        break

    product, quantity = command.split(': ')
    quantity = int(quantity)

    if product in stock:
        stock[product] += quantity
    else:
        stock[product] = quantity

total_products = len(stock)
total_quantity = sum(stock.values())
print(f"Products in stock:")

for product, quantity in stock.items():
    print(f'- {product}: {quantity}')

print(f"Total Products: {total_products}")
print(f' Total Quantity: {total_quantity}')