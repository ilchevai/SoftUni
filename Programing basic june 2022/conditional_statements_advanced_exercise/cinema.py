type_projection = input().lower()
row = int(input())
column = int(input())
hall = row * column
money = 0
if type_projection == "premiere":
    money = hall * 12
elif type_projection == "normal":
    money = hall * 7.50
elif type_projection == "discount":
    money = hall * 5
print(f"{money:.2f} leva.")