import random
print("Welcome to stone, scissor and paper!!!")
print("Enjoy!!!")
score = 0
win = 0
lost = 0
equal = 0
gamer_try = 0

while True:
    choose = ["stone", "scissor", "paper"]
    gamer_try += 1

    if gamer_try > 5:
        if score >= 7:
            print(f"Congratulations!!!"
                  f" You win this game whit {score} points."
                  f"Your wins - {win}, lost - {lost} and equals - {equal} ")
        else:
            print(f"You lost this game with {score} points."
                  f"Your wins - {win}, lost - {lost} and equals - {equal} "                  
                  f"Try again!!!")
        break
    gamer = input().lower()
    if gamer == "quit":
        break
    if gamer == "stone":
        computer = random.choice(choose)
        if computer == "stone":
            equal += 1
            score += 1
            print(f"{computer}")
            print(f"Nobody win! Your points are {score}")
        if computer == "scissor":
            win += 1
            score += 2
            print(f"{computer}")
            print(f"You win! Your points are {score}")
        if computer == "paper":
            lost += 1
            score -= 2
            print(f"{computer}")
            print(f"You lost! Your points are {score}")
    if gamer == "scissor":
        computer = random.choice(choose)
        if computer == "scissor":
            equal += 1
            score += 1
            print(f"{computer}")
            print(f"Nobody win! Your points are {score}")
        if computer == "paper":
            win += 1
            score += 2
            print(f"{computer}")
            print(f"You win! Your points are {score}")
        if computer == "stone":
            lost += 1
            score -= 2
            print(f"{computer}")
            print(f"You lost! Your points are {score}")
    if gamer == "paper":
        computer = random.choice(choose)
        if computer == "paper":
            equal += 1
            score += 1
            print(f"{computer}")
            print(f"Nobody win! Your points are {score}")
        if computer == "stone":
            win += 1
            score += 2
            print(f"{computer}")
            print(f"You win! Your points are {score}")
        if computer == "scissor":
            lost += 1
            score -= 2
            print(f"{computer}")
            print(f"You lost! Your points are {score}")




