all_balls = int(input())
points = 0
white_ball = 0
orange_ball = 0
yellow_ball = 0
red_ball = 0
black_ball = 0
other = 0
for ball in range(all_balls):
    color = input()
    if color == "red":
        red_ball += 1
        points += 5
    elif color == "orange":
        orange_ball += 1
        points += 10
    elif color == "yellow":
        yellow_ball += 1
        points += 15
    elif color == "white":
        white_ball += 1
        points += 20
    elif color == "black":
        black_ball += 1
        points //= 2
    else:
        other += 1
print(f"Total points: {points}")
print(f"Red balls: {red_ball}")
print(f"Orange balls: {orange_ball}")
print(f"Yellow balls: {yellow_ball}")
print(f"White balls: {white_ball}")
print(f"Other colors picked: {other}")
print(f"Divides from black balls: {black_ball}")
