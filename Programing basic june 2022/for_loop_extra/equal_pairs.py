n = int(input())
pair_1 = int(input()) + int(input())
pair_2 = 0
diff = 0

for _ in range(n - 1):
    pair_2 = int(input()) + int(input())
    if pair_1 == pair_2:
        continue
    elif pair_1 != pair_2:
        if abs(pair_1 - pair_2) > diff:
            diff = abs(pair_1 - pair_2)
        pair_1 = pair_2

if diff != 0:
    print(f"No, maxdiff={diff}")
elif diff == 0:
    print(f"Yes, value={pair_1}")
