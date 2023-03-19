x_hight_house = float(input())
y_light_wall = float(input())
h_hight_triangle = float(input())
side_wall = (x_hight_house * y_light_wall) - 1.5 * 1.5
two_side_walls = side_wall * 2
front_wall = (x_hight_house * x_hight_house) - 1.2 * 2
front_and_back_walls = front_wall + x_hight_house * x_hight_house
area_house = two_side_walls +front_and_back_walls
green_paint = area_house / 3.4
two_side_rooftop = 2 * (x_hight_house * y_light_wall)
front_and_back_rooftop = 2 * (x_hight_house * h_hight_triangle / 2)
area_rooftop = two_side_rooftop + front_and_back_rooftop
red_paint = area_rooftop / 4.3
print(f"{green_paint:.2f}")
print(f"{red_paint:.2f}")