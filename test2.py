party_price = float(input())
love_letters = int(input())
wax_roses = int(input())
keychains = int(input())
caricatures = int(input())
lucky_surprises = int(input())

price_love_letter = 0.60
price_wax_rose = 7.20
price_keychain = 3.60
price_caricature = 18.20
price_lucky_surprise = 22.00

total_amount = (love_letters * price_love_letter) + (wax_roses * price_wax_rose) + (keychains * price_keychain) + \
              (caricatures * price_caricature) + (lucky_surprises * price_lucky_surprise)

total_items = love_letters + wax_roses + keychains + caricatures + lucky_surprises

if total_items >= 25:
    total_amount *= 0.65

total_amount -= total_amount * 0.1

if total_amount >= party_price:
    print(f"Yes! {total_amount - party_price:.2f} lv left.")
else:
    print(f"Not enough money! {party_price - total_amount:.2f} lv needed.")
