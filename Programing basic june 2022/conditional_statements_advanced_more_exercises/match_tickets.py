budget = float(input())
category = input()
number_people = int(input())
transport = 0
leave_money = 0

if 1 <= number_people <= 4:
    transport = budget * 0.75
    if category == "Normal":
        leave_money = transport + number_people * 249.99
    elif category == "VIP":
        leave_money = transport + number_people * 499.99
elif 5 <= number_people <= 9:
    transport = budget * 0.60
    if category == "Normal":
        leave_money = transport + number_people * 249.99
    elif category == "VIP":
        leave_money = transport + number_people * 499.99
elif 10 <= number_people <= 24:
    transport = budget * 0.50
    if category == "Normal":
        leave_money = transport + number_people * 249.99
    elif category == "VIP":
        leave_money = transport + number_people * 499.99
elif 25 <= number_people <= 49:
    transport = budget * 0.40
    if category == "Normal":
        leave_money = transport + number_people * 249.99
    elif category == "VIP":
        leave_money = transport + number_people * 499.99
elif number_people >= 50:
    transport = budget * 0.25
    if category == "Normal":
        leave_money = transport + number_people * 249.99
    elif category == "VIP":
        leave_money = transport + number_people * 499.99

difference = budget - leave_money
if difference >= 0:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(difference):.2f} leva.")

