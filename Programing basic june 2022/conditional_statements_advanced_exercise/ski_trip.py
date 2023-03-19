holiday = int(input())
kind_of_room = input()
evaluation = input()
night = holiday - 1
price = 0

if kind_of_room == "room for one person":
    price = night * 18
elif kind_of_room == "apartment":
    price = night * 25
    if holiday < 10:
        price *= 0.70
    elif 10 <= holiday <= 15:
        price *= 0.65
    else:
        price *= 0.50
elif kind_of_room == "president apartment":
    price = night * 35
    if holiday < 10:
        price *= 0.90
    elif 10 <= holiday <= 15:
        price *= 0.85
    else:
        price *= 0.80
if evaluation == "positive":
    price *= 1.25
elif evaluation == "negative":
    price *= 0.90
print(f"{price:.2f}")
