expected_money = int(input())
counter_pay = 0
pay_by_card = 0
pay_cash = 0
average_card = 0
average_cash = 0
while expected_money > 0:
    command = input()
    if command == "End":
        print(f"Failed to collect required money for charity.")
        break

    counter_pay += 1
    command = int(command)
    if counter_pay % 2 == 0:
        if command >= 10:
            expected_money -= command
            pay_by_card += 1
            average_card += command
            print("Product sold!")
        else:
            print("Error in transaction!")
    else:
        if command <= 100:
            expected_money -= command
            pay_cash += 1
            average_cash += command
            print("Product sold!")
        else:
            print("Error in transaction!")
if pay_by_card != 0:
    average_pay_by_card = average_card / pay_by_card
else:
    average_pay_by_card = 0
if pay_cash != 0:
    average_pay_cash = average_cash / pay_cash
else:
    average_pay_cash = 0
if expected_money <= 0:
    print(f"Average CS: {average_pay_cash:.2f}")
    print(f"Average CC: {average_pay_by_card:.2f}")