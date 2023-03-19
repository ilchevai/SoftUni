juniors = int(input())
seniors = int(input())
rout = input()
people = juniors + seniors
money = 0

if rout == "trail":
    money = (juniors * 5.50 + seniors * 7) * 0.95
elif rout == "cross-country":
    money = (juniors * 8 + seniors * 9.50) * 0.95
    if people >= 50:
        money *= 0.75
elif rout == "downhill":
    money = (juniors * 12.25 + seniors * 13.75) * 0.95
elif rout == "road":
    money = (juniors * 20 + seniors * 21.50) * 0.95
print(f"{money:.2f}")