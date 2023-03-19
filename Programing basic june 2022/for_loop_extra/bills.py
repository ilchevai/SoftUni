month = int(input())
water = 0
internet = 0
others = 0
el = 0
for _ in range(month):
    electricity = float(input())
    el += electricity
    water += 20
    internet += 15
others += (water + internet + el) * 1.2
money = water + internet + el + others
average = money / month
print(f"Electricity: {el:.2f} lv")
print(f"Water: {water:.2f} lv")
print(f"Internet: {internet:.2f} lv")
print(f"Other: {others:.2f} lv")
print(f"Average: {average:.2f} lv")
