years_lili = int(input())
wash_machine = float(input())
price_toy = int(input())
money = 0
toy = 0

for year in range(1, years_lili + 1):
    if year % 2 == 0:
        money += 10 * year / 2
        money -= 1
    else:
        toy += 1


all_money = money + price_toy * toy
deff = abs(all_money - wash_machine)

if all_money >= wash_machine:
    print(f"Yes! {deff:.2f}")
else:
    print(f"No! {deff:.2f}")

