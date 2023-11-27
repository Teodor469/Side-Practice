string = input()
counter_n = int(input())

repeat_string = lambda string, counter_n: string * counter_n

result = repeat_string(string, counter_n)
print(result)