season = input()
km_per_month = float(input())
salary = 0

if season == "Spring" or season == "Autumn":
    if km_per_month <= 5000:
        salary = (km_per_month * 0.75) * 4
    elif 5000 < km_per_month <= 10000:
        salary = (km_per_month * 0.95) * 4
    elif 10000 < km_per_month <= 20000:
        salary = (km_per_month * 1.45) * 4
elif season == "Summer":
    if km_per_month <= 5000:
        salary = (km_per_month * 0.90) * 4
    elif 5000 < km_per_month <= 10000:
        salary = (km_per_month * 1.10) * 4
    elif 10000 < km_per_month <= 20000:
        salary = (km_per_month * 1.45) * 4
elif season == "Winter":
    if km_per_month <= 5000:
        salary = (km_per_month * 1.05) * 4
    elif 5000 < km_per_month <= 10000:
        salary = (km_per_month * 1.25) * 4
    elif 10000 < km_per_month <= 20000:
        salary = (km_per_month * 1.45) * 4
real_salary = salary * 0.90
print(f"{real_salary:.2f}")

