number_floor = int(input())
number_apartment = int(input())

apartment_num = 0
apartment_name = ""

for floor in range(number_floor, 0, -1):
    for apartment in range(number_apartment):
        apartment_num = floor * 10 + apartment

        if floor == number_floor:
            apartment_name = f"L{apartment_num} "
        elif floor % 2 == 0:
            apartment_name = f"O{apartment_num} "
        elif floor % 2 != 0:
            apartment_name = f"A{apartment_num} "

        print(apartment_name, end="")
    print()