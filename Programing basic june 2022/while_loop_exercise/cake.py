length = int(input())
weight = int(input())
size_cake = length * weight
no_take_size_cake = size_cake
number_pieces = 0
cake_finish = False
while size_cake >= 0:
    command = input()
    if command == "STOP":
        break
    pieces = int(command)
    size_cake -= pieces
    number_pieces += pieces
    if pieces > size_cake:
        cake_finish = True
diff = abs(no_take_size_cake - number_pieces)
if cake_finish:
    print(f"No more cake left! You need {diff} pieces more.")
else:
    print(f"{diff} pieces are left.")