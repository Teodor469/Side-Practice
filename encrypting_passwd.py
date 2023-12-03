# import re

# def is_valid_password(password):
#     pattern = r'^(\S+)>(\d+)\|([a-z]+)\s\|\s([A-Z]+)\s\|([^\s<>]+)<\1$'
#     match = re.match(pattern, password)
#     return bool(match)

# def encrypt_password(password):
#     match = re.match(r'^(\S+)>(\d+)\|([a-z]+)\s\|\s([A-Z]+)\s\|([^\s<>]+)<\1$', password)
#     if match:
#         encrypted_password = match.group(2) + match.group(3) + match.group(4) + match.group(5)
#         return f"Password: {encrypted_password}"
#     else:
#         return "Try another password!"

# def main():
#     n = int(input())
    
#     for _ in range(n):
#         password = input()
#         if is_valid_password(password):
#             result = encrypt_password(password)
#             print(result)
#         else:
#             print("Try another password!")

# main()

import re

def is_valid_password(password):
    pattern = r'^(?P<start>\S+)>(?P<digits>\d+)\|(?P<lower>[a-z]+)\|(?P<upper>[A-Z]+)\|(?P<symbol>[^<>]+)<(?P=start)$'
    return bool(re.match(pattern, password))

def encrypt_password(password):
    match = re.match(r'^(?P<start>\S+)>(?P<digits>\d+)\|(?P<lower>[a-z]+)\|(?P<upper>[A-Z]+)\|(?P<symbol>[^<>]+)<(?P=start)$', password)
    if match:
        encrypted_password = match.group('digits') + match.group('lower') + match.group('upper') + match.group('symbol')
        return f"Password: {encrypted_password}"
    else:
        return "Try another password!"

def main():
    n = int(input())
    
    for _ in range(n):
        password = input()
        if is_valid_password(password):
            result = encrypt_password(password)
            print(result)
        else:
            print("Try another password!")

main()
