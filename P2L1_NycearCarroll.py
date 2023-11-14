#Nycear
#11/14/2023
#mathematical expresstion and f-strings

from statistics import mean

#get input from the user
num1 =float(input("Enter a float value: "))
num2 =float(input("Enter a float value: "))
num3 =float(input("Enter a float value: "))
num4 =float(input("Enter a float value: "))

#create a empty list
num_list = []

#add value to the list
num_list.append(num1)
num_list.append(num2)
num_list.append(num3)
num_list.append(num4)

#print the list to ensure vaule are added
print(num_list)

#call methods on the ist to the sum and product
list_sum = sum(num_list)
list_avg = mean(num_list)

#output to user formated with f-string
print(f" {list_sum:.0f} {list_avg:.0f}")
print(f" {list_sum:.3f} {list_avg:.3f}")      

