from math import ceil

days_for_workout = int(input())
kilometers_first_day = float(input())
all_kilometers = 0
km_per_day = kilometers_first_day
for _ in range(days_for_workout):
    percent_more = int(input())
    percent_more /= 100
    km_per_day += km_per_day * percent_more
    all_kilometers += km_per_day
all_kilometers += kilometers_first_day
diff = abs(all_kilometers - 1000)
if all_kilometers >= 1000:
    print(f"You've done a great job running {ceil(diff)} more kilometers!")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {ceil(diff)} more kilometers")