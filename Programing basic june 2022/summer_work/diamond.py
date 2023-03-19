n = int(input())

left_dash = (n - 1) // 2
mid = n - 2 * left_dash - 2

if mid >= 0:
    stars = 2
if mid < 0:
    stars = 1
for row in range(1, n + 1):
    if n % 2 == 0 and row == n:
        break

    if row == 1 or row == n:
        print(left_dash * "-", end="")
        print(stars * "*", end="")
        print(left_dash * "-")
    else:
        print(left_dash * "-", end="")
        print("*", end="")
        print(mid * "-", end="")
        print("*", end="")
        print(left_dash * "-")
    if row <= (n - 1) // 2:
        left_dash -= 1
        mid += 2
    else:
        left_dash += 1
        mid -= 2
