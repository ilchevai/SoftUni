from math import ceil, floor

magnolia = int(input())
hyacinth = int(input())
roses = int(input())
cactus = int(input())
present = float(input())
order = magnolia * 3.25 + hyacinth * 4 + roses * 3.50 + cactus * 8
order -= order * 0.05
diffrence = abs(order - present)

if order >= present:
    print(f"She is left with {floor(diffrence)} leva.")
else:
    print(f"She will have to borrow {ceil(diffrence)} leva.")


