n = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
for p in range(n):
    num = int(input())
    if num < 200:
        p1 += 1 / n * 100
    elif 200 <= num < 400:
        p2 += 1 / n * 100
    elif 400 <= num < 600:
        p3 += 1 / n * 100
    elif 600 <= num < 800:
        p4 += 1 / n * 100
    elif num >= 800:
        p5 += 1 / n * 100
print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")
