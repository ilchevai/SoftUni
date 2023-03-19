eastern_bread = int(input())

the_best_score = 0
the_best_name = ""
for _ in range(eastern_bread):
    cooker = input()
    point = 0
    evaluation = input()
    while evaluation != "Stop":
        evaluation = int(evaluation)
        point += evaluation
        evaluation = input()
    print(f"{cooker} has {point} points.")

    if point > the_best_score:
        the_best_score = point
        the_best_name = cooker
        print(f"{the_best_name} is the new number 1!")

print(F"{the_best_name} won competition with {the_best_score} points!")


