text = input()
total_sum = 0

for n in text:
    if n == "a":
        total_sum += 1
    if n == "e":
        total_sum += 2
    if n == "i":
        total_sum += 3
    if n == "o":
        total_sum += 4
    if n == "u":
        total_sum += 5
print(total_sum)