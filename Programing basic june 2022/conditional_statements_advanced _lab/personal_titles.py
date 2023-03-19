age = float(input())
title = input()

if title == "m" and age >= 16:
    print("Mr.")
elif title == "m" and age < 16:
    print("Master")
elif title == "f" and age >= 16:
    print("Ms.")
elif title == "f" and age < 16:
    print("Miss")
