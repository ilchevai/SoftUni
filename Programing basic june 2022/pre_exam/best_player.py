best_player = ""
best_goals = 0
name = input()
while name != "END":
    goals = int(input())
    if goals > best_goals:
        best_player = name
        best_goals = goals
        if best_goals >= 10:
            break
    name = input()
print(f"{best_player} is the best player!")
if best_goals >= 3:
    print(f"He has scored {best_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {best_goals} goals.")