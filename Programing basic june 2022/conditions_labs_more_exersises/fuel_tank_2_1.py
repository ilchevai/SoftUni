type_fuel = input().lower()
liters = int(input())
card = input().lower()
price = 0
price_diesel = liters * 2.33
price_gasoline = liters * 2.22
price_gas = liters * 0.93
price_diesel_disc = liters * 2.21
price_gasoline_disc = liters * 2.04
price_gas_disc = liters * 0.85

if type_fuel == "diesel" and card == "yes":
    price = price_diesel_disc
elif type_fuel == "diesel" and card == "no":
    price = price_diesel
elif type_fuel == "gasoline" and card == "yes":
    price = price_gasoline_disc
elif type_fuel == "gasoline" and card == "no":
    price = price_gasoline
elif type_fuel == "gas" and card == "yes":
    price = price_gas_disc
elif type_fuel == "gas" and card == "no":
    price = price_gas
if 20 <= liters <= 25:
    price *= 0.92
    print(f"{price:.2f} lv.")
elif liters > 25:
    price *= 0.90
    print(f"{price:.2f} lv.")
else:
    print(f"{price:.2f} lv.")

