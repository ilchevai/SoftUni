number_group = int(input())
total_people = 0
musala = 0
monblan = 0
kilimandjaro = 0
k2 = 0
everest = 0

for _ in range(1, number_group + 1):
    ppl = int(input())
    total_people += ppl
    if ppl <= 5:
        musala += ppl
    elif 6 <= ppl <= 12:
        monblan += ppl
    elif 13 <= ppl <= 25:
        kilimandjaro += ppl
    elif 26 <= ppl <= 40:
        k2 += ppl
    elif ppl > 40:
        everest += ppl
perc_musala = musala / total_people * 100
perc_monblan = monblan / total_people * 100
perc_kilimandjaro = kilimandjaro / total_people * 100
perc_k2 = k2 / total_people * 100
perc_everest = everest / total_people * 100
print(f"{perc_musala:.2f}%")
print(f"{perc_monblan:.2f}%")
print(f"{perc_kilimandjaro:.2f}%")
print(f"{perc_k2:.2f}%")
print(f"{perc_everest:.2f}%")
