budget = float(input())
season = input()
where = ""
destination = ""
if season == "summer":
    where = "Camp"
    if budget <= 100:
        destination = "Bulgaria"
        budget *= 0.30
    elif budget <= 1000:
        destination = "Balkans"
        budget *= 0.40
    if budget > 1000:
        where = "Hotel"
        destination = "Europe"
        budget *= 0.90

if season == "winter":
    where = "Hotel"
    if budget <= 100:
        destination = "Bulgaria"
        budget *= 0.70
    elif budget <= 1000:
        destination = "Balkans"
        budget *= 0.80
    if budget > 1000:
        destination = "Europe"
        where = "Hotel"
        budget *= 0.90
print(f"Somewhere in {destination}")
print(f"{where} - {budget:.2f}")