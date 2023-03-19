from math import ceil, floor

box_paint = int(input())
wallpaper = int(input())
price_gloves = float(input())
price_brush = float(input())

gloves = ceil(wallpaper * 0.35)
brush = floor(box_paint * 0.48)
all_money = wallpaper * 5.20 + box_paint * 21.50 + gloves * price_gloves + brush * price_brush
delivery = 1 / 15 * (all_money)
print(f"This delivery will cost {delivery:.2f} lv.")