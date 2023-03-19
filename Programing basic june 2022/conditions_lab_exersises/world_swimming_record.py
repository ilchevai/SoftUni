from math import floor

record_sec = float(input())
distance_meters = float(input())
time_for_1_met = float(input())
time_for_all_distance = distance_meters * time_for_1_met
late = floor((distance_meters / 15)) * 12.5
real_time = time_for_all_distance + late
difference = abs(record_sec - real_time)

if record_sec > real_time:
    print(f" Yes, he succeeded! The new world record is {real_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {difference:.2f} seconds slower.")
