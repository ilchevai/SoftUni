budget = float(input())
season = input()
location = ""
accommodation = ""
price = 0

if budget <= 1000:
    accommodation = "Camp"
    if season == "Summer":
        price = budget * 0.65
        location = "Alaska"
    if season == "Winter":
        price = budget * 0.45
        location = "Morocco"
elif 1000 < budget <= 3000:
    accommodation = "Hut"
    if season == "Summer":
        price = budget * 0.80
        location = "Alaska"
    if season == "Winter":
        price = budget * 0.60
        location = "Morocco"
elif budget > 3000:
    accommodation = "Hotel"
    if season == "Summer":
        price = budget * 0.90
        location = "Alaska"
    if season == "Winter":
        price = budget * 0.90
        location = "Morocco"

print(f"{location} - {accommodation} - {price:.2f}")