deposit_sum = float(input())
time_deposit = int(input())
annual_interest_rate = float(input())
real_interest_rate = annual_interest_rate * 0.01
total = deposit_sum + time_deposit * ((deposit_sum * real_interest_rate) / 12 )
print(total)