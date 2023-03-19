
beginning = input()
end = input()
miss = input()
count = 0
for a in range(ord(beginning), ord(end) + 1):
    for b in range(ord(beginning), ord(end) + 1):
        for c in range(ord(beginning), ord(end) + 1):
            if a != ord(miss) and b != ord(miss) and c != ord(miss):
                print(f"{chr(a)}{chr(b)}{chr(c)}", end=" ")
                count += 1
print(count, end="")




