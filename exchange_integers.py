# Read two integer numbers
a = int(input())
b = int(input())

# Print the values before exchange
print("Before:")
print(f"a = {a}")
print(f"b = {b}")

# Exchange their values using a temporary variable
temp = a
a = b
b = temp

# Print the values after exchange
print("After:")
print(f"a = {a}")
print(f"b = {b}")
