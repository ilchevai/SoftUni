from math import floor

name_serial = input()
seasons = int(input())
episodes = int(input())
time_without_add = float(input())
add = time_without_add * 0.2
time_with_add = time_without_add + add
all_episode = seasons * episodes
all_minutes = all_episode * time_with_add + (seasons * 10)
print(f"Total time needed to watch the {name_serial} series is {floor(all_minutes)} minutes.")