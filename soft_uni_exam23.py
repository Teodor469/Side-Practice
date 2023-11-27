strings = input().split()
searched_palindrome = input()
palindromes = []

for word in strings:
    if word.lower() == word.lower()[::-1]:
        palindromes.append(word)
    

palindrome_counter = palindromes.count(searched_palindrome)
print(palindromes)
print(f"Found palindrome {palindrome_counter} times")
