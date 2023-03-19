time_first_racer = int(input())
time_second_racer = int(input())
time_third_racer = int(input())
time_in_second_all = time_first_racer + time_second_racer + time_third_racer
time_minute = time_in_second_all // 60
time_second = time_in_second_all % 60

if time_second < 10:
    print(f"{time_minute}:0{time_second}")
else:
    print(f"{time_minute}:{time_second}")