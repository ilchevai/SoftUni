student = int(input())
student1 = 0
student2 = 0
student3 = 0
student4 = 0
evolution_1 = 0
stud = 0

for _ in range(student):
    evolution = float(input())
    evolution_1 += evolution
    stud += 1
    if 2.00 <= evolution < 3.00:
        student1 += 1
    elif 3.00 <= evolution < 4.00:
        student2 += 1
    elif 4.00 <= evolution < 5.00:
        student3 += 1
    elif evolution >= 5.00:
        student4 += 1

prc_stud_1 = student1 / stud * 100
prc_stud_2 = student2 / stud * 100
prc_stud_3 = student3 / stud * 100
prc_stud_4 = student4 / stud * 100
average = evolution_1 / stud
print(f"Top students: {prc_stud_4:.2f}%")
print(f"Between 4.00 and 4.99: {prc_stud_3:.2f}%")
print(f"Between 3.00 and 3.99: {prc_stud_2:.2f}%")
print(f"Fail: {prc_stud_1:.2f}%")
print(f"Average: {average:.2f}")