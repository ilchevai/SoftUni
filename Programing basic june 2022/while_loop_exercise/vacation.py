money_trip = float(input())
hand_money = float(input())
spending_days = False
count_spending = 0
count_days = 0
while hand_money < money_trip:
    action = input()
    money = float(input())
    count_days += 1
    if action == "spend":
        count_spending += 1
        if count_spending == 5:
            spending_days = True
            break
        hand_money -= money
        if hand_money < 0:
            hand_money = 0
    else:
        count_spending = 0
        hand_money += money
if spending_days:
    print(f"You can't save the money.")
    print(f"{count_days}")
else:
    print(f"You saved the money for {count_days} days.")