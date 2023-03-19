degree = int(input())
day = input().lower()
outfit = ""
shoes = ""
if 10 <= degree <= 18:
    if day == "morning":
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    elif day == "afternoon" or day == "evening":
        outfit = "Shirt"
        shoes = "Moccasins"
elif 18 < degree <= 24:
    if day == "morning" or day == "evening":
        outfit = "Shirt"
        shoes = "Moccasins"
    elif day == "afternoon":
        outfit = "T-Shirt"
        shoes = "Sandals"
elif degree >= 25:
    if day == "morning":
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif day == "afternoon":
        outfit = "Swim Suit"
        shoes = "Barefoot"
    elif day == "evening":
        outfit = "Shirt"
        shoes = "Moccasins"

print(f"It's {degree} degrees, get your {outfit} and {shoes}.")

