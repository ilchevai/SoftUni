from math import floor

tournament = int(input())
start_points = int(input())
point = start_points
position = 0
percentage = 0

for _ in range(tournament):
    position_tournament = input()
    if position_tournament == "W":
        point += 2000
        position += 1
        percentage = position / tournament * 100
    elif position_tournament == "F":
        point += 1200
    elif position_tournament == "SF":
        point += 720

average_point = (point - start_points) / tournament

print(f"Final points: {point}")
print(f"Average points: {floor(average_point)}")
print(f"{percentage:.2f}%")