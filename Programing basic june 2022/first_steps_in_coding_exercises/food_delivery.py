number_chiken_menu = int(input())
number_fish_menu = int(input())
number_vegetarian_menu = int(input())
cost_chiken_menu = number_chiken_menu * 10.35
cost_fish_menu = number_fish_menu * 12.40
cost_vegetarian_menu = number_vegetarian_menu * 8.15
total_cost_menu = cost_chiken_menu + cost_fish_menu + cost_vegetarian_menu
dessert = total_cost_menu * 0.20
total_cost = total_cost_menu + dessert + 2.50
print(f"{total_cost:.2f}")
