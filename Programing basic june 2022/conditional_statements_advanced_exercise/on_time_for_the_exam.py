hour_exam = int(input())
minutes_exam = int(input())
hour_arrive = int(input())
minutes_arrive = int(input())
time_exam = hour_exam * 60 + minutes_exam
time_arrive = hour_arrive * 60 + minutes_arrive
difference = abs(time_arrive - time_exam)
time = 0

if time_exam > time_arrive + 30:
    print("Early")
    if difference < 60:
        print(f"{difference} minutes before the start")
    else:
        time_h = difference // 60
        time_m = difference % 60
        print(f"{time_h}:{time_m:02d} hours before the start")
elif time_exam == time_arrive:
    print("On time")
elif time_exam > time_arrive:
    print("On time")
    print(f"{difference} minutes before the start")
if time_exam < time_arrive:
    print("Late")
    if difference < 60:
        print(f"{difference} minutes after the start")
    else:
        time_h = difference // 60
        time_m = difference % 60
        print(f"{time_h}:{time_m:02d} hours after the start")
