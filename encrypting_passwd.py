import re

def validate_and_encrypt_passwords():
    n = int(input())
    pattern = r'^(\S+)>(\d+)\|([a-z]+)\|([A-Z]+)\|([^\s<>]+)<\1$'
    for _ in range(n):
        password = input()
        match = re.match(pattern, password)
        if match:
            encrypted_password = ''.join(match.groups()[1:])
            print(f'Password: {encrypted_password}')
        else:
            print('Try another password!')

validate_and_encrypt_passwords()
