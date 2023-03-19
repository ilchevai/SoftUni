n = int(input())
right_sum = 0
left_sum = 0

for _ in range(n):
    num = int(input())
    right_sum += num
for _ in range(n):
    num = int(input())
    left_sum += num

diff = abs(right_sum - left_sum)

if right_sum == left_sum:
    print(f"Yes, sum = {right_sum}")
else:
    print(f"No, diff = {diff}")