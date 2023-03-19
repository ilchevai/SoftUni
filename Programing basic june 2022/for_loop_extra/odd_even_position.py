import sys

n = int(input())
count = 0
count_1 = 0
number_odd_min = 0
number_odd_max = 0
number_even_min = 0
number_even_max = 0
max_num_odd = -sys.maxsize
min_num_odd = sys.maxsize
max_num_even = -sys.maxsize
min_num_even = sys.maxsize

for i in range(1, n + 1):
    num = float(input())
    if i % 2 != 0:
        count += num
        if num < min_num_odd:
            min_num_odd = num
            number_odd_min = num
        if num > max_num_odd:
            max_num_odd = num
            number_odd_max = num

    elif i % 2 == 0:
        count_1 += num
        if num < min_num_even:
            min_num_even = num
            number_even_min = num
        if num > max_num_even:
            max_num_even = num
            number_even_max = num

print(f"OddSum={count:.2f},")
if number_odd_min != min_num_odd:
    print("OddMin=No,")
else:
    print(f"OddMin={number_odd_min:.2f},")
if number_odd_max != max_num_odd:
    print("OddMax=No,")
else:
    print(f"OddMax={number_odd_max:.2f},")
print(f"EvenSum={count_1:.2f},")
if number_even_min != min_num_even:
    print("EvenMin=No,")
else:
    print(f"EvenMin={number_even_min:.2f},")
if number_even_max != max_num_even:
    print("EvenMax=No")
else:
    print(f"EvenMax={number_even_max:.2f}")