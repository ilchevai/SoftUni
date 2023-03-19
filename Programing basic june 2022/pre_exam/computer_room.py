mounth = input()
spend_hours = int(input())
people = int(input())
time = input()
money = 0
money_all = 0

if mounth == "march" or mounth == "april" or mounth == "may":
    if time == "day":
        one_hour = 10.50
        if people >= 4:
            money = one_hour * 0.90
        else:
            money = one_hour
        if spend_hours >= 5:
            money *= 0.50
    elif time == "night":
        one_hour = 8.40
        if people >= 4:
            money = one_hour * 0.90
        else:
            money = one_hour
        if spend_hours >= 5:
            money *= 0.50
if mounth == "june" or mounth == "july" or mounth == "august":
    if time == "day":
        one_hour = 12.60
        if people >= 4:
            money = one_hour * 0.90
        else:
            money = one_hour
        if spend_hours >= 5:
            money *= 0.50
    elif time == "night":
        one_hour = 10.20
        if people >= 4:
            money = one_hour * 0.90
        else:
            money = one_hour
        if spend_hours >= 5:
            money *= 0.50

money_all = money * people * spend_hours
print(f"Price per person for one hour: {money:.2f}")
print(f"Total cost of the visit: {money_all:.2f}")