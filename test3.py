num_dancers = int(input())
points = float(input())
season = input()
location = input()

prize_money = num_dancers * points

if location == "Bulgaria":
    prize_money *= 1
    if season == "summer":
        prize_money -= prize_money * 0.05
    elif season == "winter":
        prize_money -= prize_money * 0.08
elif location == "Abroad":
    prize_money *= 1.5
    if season == "summer":
        prize_money -= prize_money * 0.1
    elif season == "winter":
        prize_money -= prize_money * 0.15

charity_amount = prize_money * 0.75
remaining_money = prize_money - charity_amount
money_per_dancer = remaining_money / num_dancers

print(f"Charity - {charity_amount:.2f}")
print(f"Money per dancer - {money_per_dancer:.2f}")
