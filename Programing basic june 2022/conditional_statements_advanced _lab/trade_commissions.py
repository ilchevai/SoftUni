city = input().lower()
sale = float(input())
comision = 0
error_condition = False
if city == "sofia":
    if 0 <= sale <= 500:
        comision = sale * 0.05
    elif 500 < sale <= 1000:
        comision = sale * 0.07
    elif 1000 < sale <= 10000:
        comision = sale * 0.08
    elif sale > 10000:
        comision = sale * 0.12
    else:
        error_condition is True
        print("error")
elif city == "varna":
    if 0 <= sale <= 500:
        comision = sale * 0.045
    elif 500 < sale <= 1000:
        comision = sale * 0.075
    elif 1000 < sale <= 10000:
        comision = sale * 0.10
    elif sale > 10000:
        comision = sale * 0.13
    else:
        error_condition = True
        print("error")
elif city == "plovdiv":
    if 0 <= sale <= 500:
        comision = sale * 0.055
    elif 500 < sale <= 1000:
        comision = sale * 0.08
    elif 1000 < sale <= 10000:
        comision = sale * 0.12
    elif sale > 10000:
        comision = sale * 0.145
    else:
        error_condition = True
        print("error")
else:
    error_condition = True
    print("error")
if error_condition is not True:
    print(f"{comision:.2f}")