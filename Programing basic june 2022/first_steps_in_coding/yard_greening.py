price = 7.61
yard = float(input())
regular_price = yard * price
discount = 0.18 * regular_price
print(f"The final price is: {regular_price - discount} lv.")
print(f"The discount is: {discount} lv.")