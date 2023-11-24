n = int(input())
count_of_positives = []
sum_of_negatives = []

for i in range(n):
    data_input = int(input())
    if data_input > 0:
        count_of_positives.append(data_input)
    else:
        sum_of_negatives.append(data_input)

print(count_of_positives)
print(sum_of_negatives)        

print(f"Count of positives: {len(count_of_positives)}")
print(f"Sum of negatives: {sum(sum_of_negatives)}")