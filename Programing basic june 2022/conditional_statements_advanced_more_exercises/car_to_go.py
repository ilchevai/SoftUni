budget = float(input())
season = input()
class_car = ""
car = ""
price = 0

if budget <= 100:
    class_car = "Economy class"
    if season == "Summer":
        car = "Cabrio"
        price = budget * 0.35
    if season == "Winter":
        car = "Jeep"
        price = budget * 0.65
elif 100 < budget <= 500:
    class_car = "Compact class"
    if season == "Summer":
        car = "Cabrio"
        price = budget * 0.45
    if season == "Winter":
        car = "Jeep"
        price = budget * 0.80
else:
    class_car = "Luxury class"
    car = "Jeep"
    price = budget * 0.90

print(class_car)
print(f"{car} - {price:.2f}")

