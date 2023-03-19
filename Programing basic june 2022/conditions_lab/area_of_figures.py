from math import pi
choosed_type = str(input())


if choosed_type == "square":
    a = float(input())
    area = a * a
    print(f"{area:.3f}")
elif choosed_type == "rectangle":
    a = float(input())
    b = float(input())
    area = a * b
    print(f"{area:.3f}")
elif choosed_type == "circle":
    r = float(input())
    area = pi * r**2
    print(f"{area:.3f}")
elif choosed_type == "triangle":
    a = float(input())
    h = float(input())
    area = a * h / 2
    print(f"{area:.3f}")