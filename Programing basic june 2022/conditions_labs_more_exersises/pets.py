from math import floor, ceil

days = int(input())
food = int(input())
dog_food = float(input())
cat_food = float(input())
turtle_food = float(input())
turtle_food_kg = turtle_food / 1000
food_for_all = days * (dog_food + cat_food + turtle_food_kg)
diffrence = abs(food_for_all - food)

if food_for_all <= food:
    print(f"{floor(diffrence)} kilos of food left.")
else:
    print(f"{ceil(diffrence)} more kilos of food are needed.")