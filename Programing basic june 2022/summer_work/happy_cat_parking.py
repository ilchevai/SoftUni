number_days = int(input())
number_hours = int(input())
price = 0
total_price = 0

for day in range(1, number_days + 1):
    for hours in range(1, number_hours + 1):
        if day % 2 == 0 and hours % 2 != 0:
            price += 2.50
        elif day % 2 != 0 and hours % 2 == 0:
            price += 1.25
        else:
            price += 1
    print(f"Day: {day} - {price:.2f} leva")
    total_price += price
    price = 0
print(f"Total: {total_price:.2f} leva")
