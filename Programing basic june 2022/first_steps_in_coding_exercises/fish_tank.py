lenght = int(input())
weight = int(input())
hight = int(input())
precent_no_free_space = float(input("Enter precent of no free space: "))
volume_tank = (lenght * weight * hight) * 0.001
real_volume_tank = volume_tank * (1 - precent_no_free_space / 100)
print(real_volume_tank)
