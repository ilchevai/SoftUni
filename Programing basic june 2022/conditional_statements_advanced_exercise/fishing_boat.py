budget = int(input())
season = input()
fishers = int(input())
price = 0

if season == "Spring":
    price = 3000
    if fishers <= 6:
        price *= 0.90
    elif 7 <= fishers <= 11:
        price *= 0.85
    else:
        price *= 0.75
    if fishers % 2 == 0:
            price *= 0.95
elif season == "Summer" or season == "Autumn":
    price = 4200
    if fishers <= 6:
        price *= 0.90
    elif 7 <= fishers <= 11:
        price *= 0.85
    else:
        price *= 0.75
    if season == "Summer" and fishers % 2 == 0:
            price *= 0.95
elif season == "Winter":
    price = 2600
    if fishers <= 6:
        price *= 0.90
    elif 7 <= fishers <= 11:
        price *= 0.85
    else:
        price *= 0.75
    if fishers % 2 == 0:
            price *= 0.95

diffrence = abs(budget - price)

if price <= budget:
    print(f"Yes! You have {diffrence:.2f} leva left.")
else:
    print(f"Not enough money! You need {diffrence:.2f} leva.")
