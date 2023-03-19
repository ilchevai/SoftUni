number_cargo = int(input())
bus = 200
truck = 175
train = 120
price1 = 0
price2 = 0
price3 = 0
tons = 0
ton1 = 0
ton2 = 0
ton3 = 0

for _ in range(number_cargo):
    ton = int(input())
    tons += ton
    if ton <= 3:
        price1 += ton * bus
        ton1 += ton
    elif 3 < ton <= 11:
        price2 += ton * truck
        ton2 += ton
    elif ton >= 12:
        price3 += ton * train
        ton3 += ton

percentage1 = ton1 / tons * 100
percentage2 = ton2 / tons * 100
percentage3 = ton3 / tons * 100
average = (price1 + price2 + price3) / tons
print(f"{average:.2f}")
print(f"{percentage1:.2f}%")
print(f"{percentage2:.2f}%")
print(f"{percentage3:.2f}%")
