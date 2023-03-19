days_holiday = int(input())
kind_room = input()
evaluation = input()
nights = days_holiday - 1
price = 0
if days_holiday < 10:
    if kind_room == "room for one person":
        price = nights * 18
    if kind_room == "apartment":
        price = nights * 25
        price *= 0.70
    if kind_room == "president apartment":
        price = nights * 35
        price *= 0.90
elif 10 <= days_holiday < 15:
    if kind_room == "room for one person":
        price = nights * 18
    if kind_room == "apartment":
        price = nights * 25
        price *= 0.65
    if kind_room == "president apartment":
        price = nights * 35
        price *= 0.85
elif days_holiday >= 15:
    if kind_room == "room for one person":
        price = nights * 18
    if kind_room == "apartment":
        price = nights * 25
        price *= 0.50
    if kind_room == "president apartment":
        price = nights * 35
        price *= 0.80
if evaluation == "positive":
    price *= 1.25
else:
    price *= 0.90
print(f"{price:.2f}")