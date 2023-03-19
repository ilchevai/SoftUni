paper = int(input())
layer = int(input())
liters_gum = float(input())
percent_discount = int(input()) / 100

all_money = paper * 5.80 + layer * 7.20 + liters_gum * 1.20
real_money = all_money - all_money * percent_discount
print(f"{real_money:.3f}")