count_steps = 0

while count_steps < 10000:
    steps = input()
    if steps != "Going home":
        steps = int(steps)
        count_steps += steps
    if steps == "Going home":
        count_steps += int(input())
        break


diff = abs(10000 - count_steps)
if count_steps >= 10000:
    print(f"Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")


