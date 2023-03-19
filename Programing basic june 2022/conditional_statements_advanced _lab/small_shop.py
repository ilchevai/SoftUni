product = input()
city = input()
quatity = float(input())
price = 0

if city == "Sofia" and product == "coffee":
    price = quatity * 0.50
elif city == "Sofia" and product == "water":
    price = quatity * 0.80
elif city == "Sofia" and product == "beer":
    price = quatity * 1.20
elif city == "Sofia" and product == "sweets":
    price = quatity * 1.45
elif city == "Sofia" and product == "peanuts":
    price = quatity * 1.60
if city == "Plovdiv" and product == "coffee":
    price = quatity * 0.40
elif city == "Plovdiv" and product == "water":
    price = quatity * 0.70
elif city == "Plovdiv" and product == "beer":
    price = quatity * 1.15
elif city == "Plovdiv" and product == "sweets":
    price = quatity * 1.30
elif city == "Plovdiv" and product == "peanuts":
    price = quatity * 1.50
if city == "Varna" and product == "coffee":
    price = quatity * 0.45
if city == "Varna" and product == "water":
    price = quatity * 0.70
elif city == "Varna" and product == "beer":
    price = quatity * 1.10
elif city == "Varna" and product == "sweets":
    price = quatity * 1.35
elif city == "Varna" and product == "peanuts":
    price = quatity * 1.55
print(price)



