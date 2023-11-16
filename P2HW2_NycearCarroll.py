# CTI - 100
#P2HW2
#Nycear J. Carroll
#

from statistics import mean

module1 = float(input("enter grades: "))
module2 = float(input("enter grades: "))
module3 = float(input("enter grades: "))
module4 = float(input("enter grades: "))
module5 = float(input("enter grades: "))
module6 = float(input("enter grades: "))

module_list =[]

module_list.append(module1)
module_list.append(module2)
module_list.append(module3)
module_list.append(module4)
module_list.append(module5)
module_list.append(module6)

Lowest_grade = min(module_list)
Highest_grade = max(module_list)
Sum_grade = sum(module_list)
Avg_grade = mean(module_list)

print("---------Results---------")
print(f"Lowest of grades: {Lowest_grade:.2f}")
print(f"Highest of grades: {Highest_grade:.2f}")
print(f"Aum of grades: {Sum_grade:.2f}")
print(f"Avg of grades: {Avg_grade:.2f}")
print("--------------------------")
