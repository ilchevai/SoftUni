location = int(input())

for _ in range(location):
    gold_yield = 0
    average_gold_expect = float(input())
    days_yield = int(input())
    for _ in range(days_yield):
        gold_per_day = float(input())
        gold_yield += gold_per_day
    average_gold = gold_yield / days_yield
    if average_gold >= average_gold_expect:
        print(f"Good job! Average gold per day: {average_gold:.2f}.")
    else:
        diff = abs(average_gold - average_gold_expect)
        print(f"You need {diff:.2f} gold.")


