budget = float(input())
video_card = int(input())
processor = int(input())
ram = int(input())
money_video_card = video_card * 250
money_all = money_video_card + (processor * (money_video_card * 0.35)) + (ram * (money_video_card * 0.10))


if video_card > processor:
    money_all -= money_all * 0.15

free_money = abs(budget - money_all)
if budget >= money_all:
    print(f"You have {free_money:.2f} leva left!")
else:
    print(f"Not enough money! You need {free_money:.2f} leva more!")


