ani_book = input()
count_book = 0

while True:
    book = input()

    if book == ani_book:
        print(f"You checked {count_book} books and found it.")
        break
    if book == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {count_book} books.")
        break
    if book != ani_book:
        count_book += 1
        continue

