flower = input()
number_flower = int(input())
budget = int(input())
price = 0

if flower == "Roses":
    price = number_flower * 5
    if number_flower > 80:
        price *= 0.90
elif flower == "Dahlias":
    price = number_flower * 3.80
    if number_flower > 90:
        price *= 0.85
elif flower == "Tulips":
    price = number_flower * 2.80
    if number_flower > 80:
        price *= 0.85
elif flower == "Narcissus":
    price = number_flower * 3.00
    if number_flower < 120:
        price *= 1.15
elif flower == "Gladiolus":
    price = number_flower * 2.50
    if number_flower < 80:
        price *= 1.20
diffrence = abs(budget - price)
if price <= budget:
    print(f"Hey, you have a great garden with {number_flower} {flower} and {diffrence:.2f} leva left.")
else:
    print(f"Not enough money, you need {diffrence:.2f} leva more.")