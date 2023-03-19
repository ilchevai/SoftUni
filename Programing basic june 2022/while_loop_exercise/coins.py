num = float(input())
num = int(num * 100)
counter = 0

counter += num // 200
num %= 200
counter += num // 100
num %= 100
counter += num // 50
num %= 50
counter += num // 20
num %= 20
counter += num // 10
num %= 10
counter += num // 5
num %= 5
counter += num // 2
num %= 2
counter += num // 1
num %= 1
print(counter)

