w_length = float(input())
h_width = float(input())
length_sm = w_length * 100
width_sm = (h_width * 100) - 100
number_desk_of_leght = length_sm / 120
number_desk_of_width = width_sm / 70
all_desk = (int(number_desk_of_width) * int(number_desk_of_leght)) - 3
print(all_desk)