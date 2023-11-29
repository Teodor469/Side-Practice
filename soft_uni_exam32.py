import re

drinks_info = input()
pattern = r'(?i)([#|])([a-zA-Z\s]+)(\1)(\d{2}/\d{2}/\d{2})(\1)(\d+)(\1)'

matches = re.findall(pattern, drinks_info)

total_volume = sum([int(match[5]) for match in matches])

days_to_last = total_volume // 1000

print(f"You have drinks to last {days_to_last} days!")

for element in matches:
    drink = element[1]
    date = element[3]
    volume = element[5]
    print(f"Item: {drink}, Expired: {date}, Volume: {volume} ml")
