weight = int(input())
length = int(input())
hight = int(input())
size_free_place = weight * length * hight
no_more_free_place = False
number_boxes = 0
while size_free_place > number_boxes:
    command = input()
    if command == "Done":
        break
    boxes = int(command)
    number_boxes += boxes
    if number_boxes > size_free_place:
        no_more_free_place = True
diff = abs(number_boxes - size_free_place)
if no_more_free_place:
    print(f"No more free space! You need {diff} Cubic meters more.")
else:
    print(f"{diff} Cubic meters left.")