number_pages = int(input())
pages_for_hour = int(input())
number_of_days = int(input())
total_hours = number_pages / pages_for_hour
hour_for_reading = total_hours / number_of_days
print(int(hour_for_reading))

