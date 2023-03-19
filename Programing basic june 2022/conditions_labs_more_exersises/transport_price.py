km = int(input())
when = input()
road = 0

if when == "day":
    if km < 20:
        road = 0.70 + 0.79 * km
    if km >= 100:
        road = 0.06 * km
    if 100 > km >= 20:
        road = 0.09 * km
    print(f"{road:.2f}")
elif when == "night":
    if km >= 100:
       road = 0.06 * km
    if 100 > km >= 20:
       road = 0.09 * km
    if km < 20:
       road = 0.70 + 0.90 * km
    print(f"{road:.2f}")