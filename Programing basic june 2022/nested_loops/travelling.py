destination = input()
counter = 0
while destination != "End":
    counter = 0
    need_money = float(input())
    while counter < need_money:
        current_money = float(input())
        counter += current_money
        if counter >= need_money:
            print(f"Going to {destination}!")
    destination = input()




