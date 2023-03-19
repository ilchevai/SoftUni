inheritance = float(input())
year_to_live = int(input())
current_year = 18
left_money = inheritance

for year in range(1800, year_to_live + 1):
    if year % 2 == 0:
        left_money -= 12000
    else:
        left_money -= 12000 + 50 * current_year
    current_year += 1

if left_money >= 0:
    print(f"Yes! He will live a carefree life and will have {left_money:.2f} dollars left.")
else:
    print(f"He will need {abs(left_money):.2f} dollars to survive.")

