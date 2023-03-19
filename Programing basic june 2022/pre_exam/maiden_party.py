price_maiden_party = float(input())
love_letters = int(input())
vax_roses = int(input())
key_holder = int(input())
caricature = int(input())
lucky_surprised = int(input())
items = love_letters + vax_roses + key_holder + caricature + lucky_surprised
income = love_letters * 0.60 + vax_roses * 7.20 + key_holder * 3.60\
    + caricature * 18.20 + lucky_surprised * 22
if items >= 25:
    income *= 0.65
income *= 0.90
diff = abs(price_maiden_party - income)
if income >= price_maiden_party:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")