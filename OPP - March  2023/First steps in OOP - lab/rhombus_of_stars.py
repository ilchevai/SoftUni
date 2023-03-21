size = int(input())

for x in range(size):
    space_up = size - x - 1
    star_up = x + 1
    print(space_up * " " + star_up * "* ")
