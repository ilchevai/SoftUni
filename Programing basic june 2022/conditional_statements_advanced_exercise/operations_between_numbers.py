n_1 = int(input())
n_2 = int(input())
operator = input()
result = 0

if operator == "+":
   result = n_1 + n_2
   if result % 2 == 0:
       print(f"{n_1} {operator} {n_2} = {result} - even")
   else:
       print(f"{n_1} {operator} {n_2} = {result} - odd")
if operator == "-":
    result = n_1 - n_2
    if result % 2 == 0:
        print(f"{n_1} {operator} {n_2} = {result} - even")
    else:
        print(f"{n_1} {operator} {n_2} = {result} - odd")
if operator == "*":
    result = n_1 * n_2
    if result % 2 == 0:
        print(f"{n_1} {operator} {n_2} = {result} - even")
    else:
        print(f"{n_1} {operator} {n_2} = {result} - odd")
if operator == "/" and not n_2 == 0:
    result = n_1 / n_2
    print(f"{n_1} / {n_2} = {result:.2f}")
if operator == "%" and not n_2 == 0:
    result = n_1 % n_2
    print(f"{n_1} % {n_2} = {result}")
if (operator == "/" and n_2 == 0) or (operator == "%" and n_2 == 0):
    print(f"Cannot divide {n_1} by zero")
