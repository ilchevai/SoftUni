name_actor = input()
academy_point = float(input())
judge = int(input())
one_judge_point = academy_point

for _ in range(judge):
    name_judge = len(input())
    judge_point = float(input())
    if one_judge_point >= 1250.5:
        break
    else:
        one_judge_point += (name_judge * judge_point) / 2

if one_judge_point < 1250.5:
    diff = 1250.5 - one_judge_point
    print(f"Sorry, {name_actor} you need {diff:.1f} more!")
else:
    print(f"Congratulations, {name_actor} got a nominee for leading role with {one_judge_point:.1f}!")
