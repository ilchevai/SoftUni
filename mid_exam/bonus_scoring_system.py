from math import ceil

number_of_the_students = int(input())
number_of_the_lectures = int(input())
additional_bonus = int(input())
max_bonus = 0
attend = 0
for stud in range(number_of_the_students):
    attendance = int(input())
    total_bonus = attendance / number_of_the_lectures * (5 + additional_bonus)

    if max_bonus < total_bonus:
        max_bonus = total_bonus
        attend = attendance
    else:
        continue
print(f"Max Bonus: {ceil(max_bonus)}.")
print(f"The student has attended {attend} lectures.")
