bottles = int(input())
ml_liquid = bottles * 750
new_fill = 0
count_dish = 0
count_pot = 0

while ml_liquid >= 0:
    command = input()
    new_fill += 1
    if command == "End":
        break

    command = int(command)
    if new_fill % 3 == 0:
        ml_liquid -= command * 15
        count_pot += command
    else:
        ml_liquid -= command * 5
        count_dish += command
if ml_liquid < 0:
    print(f"Not enough detergent, {abs(ml_liquid)} ml. more necessary!")
else:
    print(f"Detergent was enough!")
    print(f"{count_dish} dishes and {count_pot} pots were washed.")
    print(f"Leftover detergent {ml_liquid} ml.")




