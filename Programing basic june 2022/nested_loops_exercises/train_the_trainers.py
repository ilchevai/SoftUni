number_judge = int(input())
command = input()
sum_grade = 0
presentation = 0
sum_average = 0
while command != "Finish":
    name_presentation = command
    for grade in range(number_judge):
        grade = float(input())
        sum_grade += grade
    average_grade = sum_grade / number_judge
    print(f"{name_presentation} - {average_grade:.2f}.")
    presentation += 1
    sum_grade = 0
    sum_average += average_grade
    command = input()
average_grade_all = sum_average / presentation
print(f"Student's final assessment is {average_grade_all:.2f}.")