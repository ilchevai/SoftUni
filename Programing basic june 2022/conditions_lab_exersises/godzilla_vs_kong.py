budget_film = float(input())
number_statist = int(input())
price_suit = float(input())
decor = budget_film * 0.10

if number_statist > 150:
    price_suit *= 0.90

money = ( number_statist * price_suit ) + decor
difference = abs(budget_film - money)
if money > budget_film:
    print(f"""Not enough money!
Wingard needs {difference:.2f} leva more.""")
if money <= budget_film:
    print(f"""Action!
Wingard starts filming with {difference:.2f} leva left.
""")