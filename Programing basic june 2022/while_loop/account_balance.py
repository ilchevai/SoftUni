
total = 0

while True:
    current_money = input()

    if current_money == "NoMoreMoney":
        break

    current_money = float(current_money)
    if current_money >= 0:
        print(f"Increase: {current_money:.2f}")
    else:
        print("Invalid operation!")
        break

    total += current_money
print(f"Total: {total:.2f}")
