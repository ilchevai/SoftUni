number_of_pens = int(input())
number_of_markers = int(input())
number_of_detergent = int(input())
persentage_discount = int(input())
package_pen = number_of_pens * 5.80
package_markers = number_of_markers * 7.20
detergent_liters = number_of_detergent * 1.20
sum = package_pen + package_markers + detergent_liters
total_sum = sum - (sum * persentage_discount * 0.01)
print(total_sum)