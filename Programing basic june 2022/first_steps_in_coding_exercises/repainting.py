needed_nylon = int(input())
needed_paint = int(input())
needed_thinner = int(input())
hours_job_done = int(input())
total_nylon = (needed_nylon + 2) * 1.50
total_paint = (needed_paint + 10/100 * needed_paint) * 14.50
total_thinner = needed_thinner * 5.00
all_money = total_thinner + total_paint + total_nylon + 0.40
money_for_master  = (all_money * 0.30) * hours_job_done
total_money = all_money + money_for_master
print(total_money)
