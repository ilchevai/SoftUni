type_fuel = input()
liters = float(input())
card = input()
price = 0

if card == "No":
    if type_fuel == "Gas":
       price= liters * 0.93
    elif type_fuel == "Gasoline":
       price = liters * 2.22
    elif type_fuel == "Diesel":
       price= liters * 2.33
if card == "Yes":
    if type_fuel == "Gas":
        price = liters * 0.85
    elif type_fuel == "Gasoline":
        price = liters * 2.04
    elif type_fuel == "Diesel":
        price = liters * 2.21
if 20 <= liters <= 25:
    price *= 0.92
    print(f"{price:.2f} lv.")
elif liters > 25:
    price *= 0.90
    print(f"{price:.2f} lv.")
else:
    print(f"{price:.2f} lv.")