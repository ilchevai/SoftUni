last_sector = input()
rows_firs_sector = int(input())
places_odd_rows = int(input())
count = 0
seats = 0
for sector in range(ord('A'), ord(last_sector) + 1):
    rows_firs_sector += 1
    for row in range(1, rows_firs_sector):
        if row % 2 != 0:
            place = places_odd_rows
        else:
            place = places_odd_rows + 2
        for pl in range(place):
            for i in range(ord('a'), ord('z') + 1):
                count += 1
                if count > place:
                    break
                print(f"{chr(sector)}{row}{chr(i)}")
                seats += 1
        count = 0
print(seats)





