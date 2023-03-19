range_num = int(input())
counter = 0

for _ in range(range_num):
    num = int(input())
    counter += num
    average = counter / range_num
print(f"{average:.2f}")