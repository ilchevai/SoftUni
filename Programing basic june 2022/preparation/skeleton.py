min_control = int(input())
sec_control = int(input())
meters_chute = float(input())
sec_for_100_m = int(input())

control_in_sec = min_control * 60 + sec_control
meters = meters_chute / 100
slow = meters_chute / 120
time = (sec_for_100_m * meters) - slow * 2.5
if time <= control_in_sec:
    print(f"Marin Bangiev won an Olympic quota!")
    print(f"His time is {time:.3f}.")
else:
    diff = abs(control_in_sec - time)
    print(f"No, Marin failed! He was {diff:.3f} second slower.")

