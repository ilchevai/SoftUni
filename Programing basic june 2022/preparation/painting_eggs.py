size_egg = input()
colour_egg = input()
parcel = int(input())
money = 0

if size_egg == "Large" and colour_egg == "Red":
    money = 16 * parcel
elif size_egg == "Medium" and colour_egg == "Red":
    money = 13 * parcel
elif size_egg == "Small" and colour_egg == "Red":
    money = 9 * parcel
elif size_egg == "Large" and colour_egg == "Green":
    money = 12 * parcel
elif size_egg == "Medium" and colour_egg == "Green":
    money = 9 * parcel
elif size_egg == "Small" and colour_egg == "Green":
    money = 8 * parcel
elif size_egg == "Large" and colour_egg == "Yellow":
    money = 9 * parcel
elif size_egg == "Medium" and colour_egg == "Yellow":
    money = 7 * parcel
elif size_egg == "Small" and colour_egg == "Yellow":
    money = 5 * parcel
real_money = money * 0.65
print(f"{real_money:.2f} leva.")