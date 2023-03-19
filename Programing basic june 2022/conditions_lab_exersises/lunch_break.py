from math import ceil

name_serial = input()
time = int(input())
break_time = int(input())
lunch_time = 1/8 * break_time + 1/4 * break_time
serial_time = abs(break_time - lunch_time)
need_time = abs(serial_time - time)

if time <= serial_time:
    print(f"You have enough time to watch {name_serial} and left with {ceil(need_time)} minutes free time.")
else:
   print(f"You don't have enough time to watch {name_serial}, you need {ceil(need_time)} more minutes.")