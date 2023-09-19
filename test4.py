N = int(input())
M = float(input())

total_distance = M
for _ in range(N):
    percentage = int(input())
    distance_increase = M * (percentage / 100)
    total_distance += distance_increase

if total_distance >= 1000:
    print(f"You've done a great job running {total_distance - 1000:.0f} more kilometers!")
else:
    remaining_distance = 1000 - total_distance
    print(f"Sorry Mrs. Ivanova, you need to run {remaining_distance:.0f} more kilometers")
































