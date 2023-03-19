period = int(input())
treat = 0
untreat = 0
doctors = 7

for _ in range(1, period + 1):
    if untreat > treat and _ % 3 == 0:
            doctors += 1
    patients = int(input())
    if patients <= doctors:
        treat += patients
    else:
        untreat += (patients - doctors)
        treat += doctors

print(f"Treated patients: {treat}.")
print(f"Untreated patients: {untreat}.")