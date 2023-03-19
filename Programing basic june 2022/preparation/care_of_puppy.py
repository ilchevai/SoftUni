bought_food_kg = int(input())
eat = input()
left_food = 0
bought_food_grams = bought_food_kg * 1000
while eat != "Adopted":
    eat = int(eat)
    bought_food_grams -= eat
    eat = input()
if bought_food_grams >= 0:
    print(f"Food is enough! Leftovers: {bought_food_grams} grams.")
else:
    print(f"Food is not enough. You need {abs(bought_food_grams)} grams more.")