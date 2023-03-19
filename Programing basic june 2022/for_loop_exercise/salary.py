open_tab = int(input())
salary = int(input())

facebook = 150
instagram = 100
reddit = 50

for tab in range(open_tab):
    tab1 = input()
    if tab1 == "Facebook":
        salary -= facebook
    if tab1 == "Instagram":
        salary -= instagram
    if tab1 == "Reddit":
        salary -= reddit
if salary <= 0:
    print("You have lost your salary.")
else:
    diff = abs(salary)
    print(f"{diff}")