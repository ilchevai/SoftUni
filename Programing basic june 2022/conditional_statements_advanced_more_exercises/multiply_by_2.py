i = 0
while i >= 0:
    i = float(input())
    if i < 0:
        print("Negative number!")
        break
    i *= 2
    print(f"Result: {i:.2f}")
