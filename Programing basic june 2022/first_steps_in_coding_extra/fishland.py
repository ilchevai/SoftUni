price_mackerel_per_kg = float(input())
price_sprat_per_kg = float(input())
kg_bonito = float(input())
kg_horse_mackerel = float(input())
kg_mussels = float(input())
price_mussels_per_kg = 7.50
price_bonito_per_kg = price_mackerel_per_kg + price_mackerel_per_kg * 0.60
price_horse_mackerel_per_kg = price_sprat_per_kg + price_sprat_per_kg * 0.80
total_price = price_bonito_per_kg * kg_bonito + price_horse_mackerel_per_kg * kg_horse_mackerel\
    + price_mussels_per_kg * kg_mussels
print(f"{total_price:.2f}")