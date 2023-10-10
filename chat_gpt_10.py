command = input()
total_price = 0
total_price_after_discount = 0

while command != 'checkout':
    items = float(command)

    if items > 0:
        total_price += items

    command = input()

if total_price >= 100:
    total_price_after_discount = total_price * 0.90
    print(f'This is the total price without discount: {total_price}')
    print(f'This is the total price with the discount: {total_price_after_discount}')
else:
    print(f'This is the total price: {total_price}')