command = input()
kids = 0
adult = 0
money_toys = 0
money_sweater = 0
while command != "Christmas":
    command = int(command)
    if command <= 16:
        kids += 1
        money_toys += 5
    else:
        adult += 1
        money_sweater += 15

    command = input()

print(f"Number of adults: {adult}" )
print(f"Number of kids: {kids}")
print(f"Money for toys: {money_toys}")
print(f"Money for sweaters: {money_sweater}")