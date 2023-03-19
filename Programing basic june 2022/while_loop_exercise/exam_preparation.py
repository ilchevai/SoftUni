max_bad_grade = int(input())
bad_counter = 0
average_grade = 0
problem_solved = 0
last_exam = ""
is_expelled = False
exam = input()
while exam != "Enough":
    grade = int(input())
    if grade <= 4:
        bad_counter += 1
        if bad_counter == max_bad_grade:
            is_expelled = True
            break

    problem_solved += 1
    average_grade += grade
    last_exam = exam

    exam = input()

if is_expelled:
    print(f"You need a break, {bad_counter} poor grades.")
else:
    average_grade /= problem_solved
    print(f"Average score: {average_grade:.2f}")
    print(f"Number of problems: {problem_solved}")
    print(f"Last problem: {last_exam}")




