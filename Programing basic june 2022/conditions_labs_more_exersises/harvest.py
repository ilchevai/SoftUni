from math import floor, ceil

vineyard = int(input())
grape_per_met = float(input())
need_liters_vine = int(input())
employers = int(input())
harvest = vineyard * grape_per_met
harvest_for_vine = harvest * 40 / 100
liters_vine = harvest_for_vine / 2.5
the_rest = abs(need_liters_vine - liters_vine)
liters_for_empl = the_rest / employers

if liters_vine < need_liters_vine:
    print(f"It will be a tough winter! More {floor(the_rest)} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {floor(liters_vine)} liters.")
    print(f"{ceil(the_rest)} liters left -> {ceil(liters_for_empl)} liters per person.")