from math import floor

width_spaceship = float(input())
length_spaceship = float(input())
height_spaceship = float(input())
average_height_astro = float(input())

volume_spaceship = width_spaceship * length_spaceship * height_spaceship
volume_one_room = 2 * 2 * (average_height_astro + 0.40)
astro = floor(volume_spaceship / volume_one_room)
if astro < 3:
    print("The spacecraft is too small.")
if astro > 10:
    print("The spacecraft is too big.")
if 3 <= astro <= 10:
    print(f"The spacecraft holds {astro} astronauts.")