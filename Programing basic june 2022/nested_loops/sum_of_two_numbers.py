start_interval = int(input())
end_interval = int(input())
magic_num = int(input())
counter = 0
number = False
for x in range(start_interval, end_interval + 1):
    for y in range(start_interval, end_interval + 1):
        counter += 1
        if x + y == magic_num:
            number = True
            print(f"Combination N:{counter} ({x} + {y} = {magic_num})")
            break
    if number:
        break
if not number:
    print(f"{counter} combinations - neither equals {magic_num}")