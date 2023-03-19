a = float(input())

if 5.00 <= a <= 11.9:
    print("Cold")
elif 12.00 <= a <= 14.9:
    print("Cool")
elif 15.00 <= a <= 20.00:
     print("Mild")
elif 20.1 <= a <= 25.9:
     print("Warm")
elif 26.00 <= a <= 35.00:
     print("Hot")
else:
     print("unknown")