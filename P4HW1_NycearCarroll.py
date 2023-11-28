# CTI - 100
#P2HW2
#Nycear J. Carroll
#Use loop to get user input 

from statistics import mean

#get number of grades from user 
num_module = int(input("how man grades will you enter? "))

#create a list to store the grades 
module_list =[]

#get grades fron the user
for i in range(num_module):
    module = float(input(f"enter grades {i + 1}:. "))
    module_list.append(module)
print(module_list)
"""
#get input from user
module1 = float(input("enter grades 1: "))
module2 = float(input("enter grades 2: "))
module3 = float(input("enter grades 3: "))
module4 = float(input("enter grades 4: "))
module5 = float(input("enter grades 5: "))
module6 = float(input("enter grades 6: "))

#create a list to store the grades 
module_list =[]

#add values to the list
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
"""
