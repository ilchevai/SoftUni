free_days = int(input())
work_days = 365 - free_days
play_work = work_days * 63
play_free = free_days * 127
play = play_free + play_work
diffrence = abs(play - 30000)
hour = diffrence // 60
minutes = diffrence % 60

if play > 30000:
    print("Tom will run away")
    print(f"{hour} hours and {minutes} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{hour} hours and {minutes} minutes less for play")