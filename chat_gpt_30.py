# a = input()
# stack = []

# for index in range(len(a)):
#     if a[index] == '(':
#         stack.append(index)
#     elif a[index] == ')':
#         start_index = stack.pop()
#         end_index = index + 1
#         print(a[start_index:end_index])
        

def is_balanced_parentheses(s: str) -> bool:
    stack = []

    for index in range(len(s)):
        if s[index] == '(':
            stack.append(index)
        elif s[index] == ')':
            if not stack:
                return False
            stack.pop()
    return not stack
    
print(is_balanced_parentheses("((()))"))