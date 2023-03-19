name = input()
counter_class = 0
evaluation_all = 0
fail = 0

while True:
    evaluation = float(input())
    counter_class += 1
    if evaluation < 4:
        fail += 1
        if fail == 2:
            print(f"{name} has been excluded at {counter_class} grade")
            break
        else:
            counter_class -= 1
            continue
    if evaluation >= 4:
        if counter_class < 12:
            evaluation_all += evaluation
        else:
            evaluation_all += evaluation
            break

average = evaluation_all / counter_class
if counter_class == 12:
    print(f"{name} graduated. Average grade: {average:.2f}")

