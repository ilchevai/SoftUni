price_for_kg_vegetables = float(input())
price_for_kg_fruits = float(input())
all_kg_vegetables = int(input())
all_kg_fruits = int(input())
income_from_market = (price_for_kg_fruits * all_kg_fruits) + (price_for_kg_vegetables * all_kg_vegetables)
income_euro = income_from_market / 1.94
print(f"{income_euro:.2f}")