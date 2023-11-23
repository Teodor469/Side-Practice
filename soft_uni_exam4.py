string_of_integers = input().split(', ')
count_of_beggars = int(input())

integer_list = [int(number) for number in string_of_integers]

final_sum = [0] * count_of_beggars

for i, num in enumerate(integer_list):
    beggar_index = i % count_of_beggars
    final_sum[beggar_index] += num

print(final_sum)