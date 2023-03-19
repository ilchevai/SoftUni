month = input()
number_days = int(input())
price_studio = 0
price_apartment = 0

if month == "May" or month == "October":
    price_apartment = number_days * 65
    price_studio = number_days * 50
    if number_days > 14:
        price_studio *= 0.70
        price_apartment *= 0.90
    elif number_days > 7:
        price_studio *= 0.95
if month == "June" or month == "September":
    price_apartment = number_days * 68.70
    price_studio = number_days * 75.20
    if number_days > 14:
        price_apartment *= 0.90
        price_studio *= 0.80
if month == "July" or month == "August":
    price_apartment = number_days * 77
    price_studio = number_days * 76
    if number_days > 14:
        price_apartment *= 0.90
print(f"Apartment: {price_apartment:.2f} lv.")
print(f"Studio: {price_studio:.2f} lv.")
