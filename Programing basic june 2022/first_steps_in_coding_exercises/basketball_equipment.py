one_year_tax = int(input())
basketball_shoes = one_year_tax * 0.60
basketball_clothes = basketball_shoes - basketball_shoes * 20/100
basketball_ball = basketball_clothes * 1/4
basketball_accssesoaries = basketball_ball * 1/5
money_for_one_year = one_year_tax + basketball_shoes + basketball_clothes + basketball_ball +\
basketball_accssesoaries
print(money_for_one_year)