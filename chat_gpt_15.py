first_string = input()
second_string = input()

first_string = first_string.lower()
second_string = second_string.lower()

if sorted(first_string) == sorted(second_string):
    print("Anagrams")
else:
    print("Not Anagrams")