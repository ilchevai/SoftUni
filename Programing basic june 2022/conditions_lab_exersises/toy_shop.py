price_for_trip = float(input())
number_puzzles = int(input())
number_dolls = int(input())
number_bears = int(input())
number_minions = int(input())
number_trucks = int(input())
final_money = number_puzzles * 2.60 + number_dolls * 3 + number_bears * 4.10 + number_minions * 8.20 + number_trucks * 2
number_order = number_puzzles + number_dolls + number_bears + number_minions + number_trucks

if number_order >= 50:
    final_money = (final_money - final_money * 0.25)
rent_money = final_money * 0.1
final_money = final_money - rent_money
miss_money = abs(final_money - price_for_trip)

if final_money >= price_for_trip:
    print(f"Yes! {miss_money:.2f} lv left.")
else:
    print(f"Not enough money! {miss_money:.2f} lv needed.")
