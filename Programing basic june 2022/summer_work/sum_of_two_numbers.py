start_interval = int(input())
end_interval = int(input())
magic_number = int(input())
combination = 0

find = False

for num1 in range(start_interval, end_interval + 1):
    for num2 in range(start_interval, end_interval + 1):
        sumary = num1 + num2
        combination += 1
        if sumary == magic_number:
            find = True
            break
    if find:
        break

if find:
    print(f"Combination N:{combination} ({num1} + {num2} = {magic_number})")
else:
    print(f"{combination} combinations - neither equals {magic_number}")
