#CTI-110
#P3HW2 - Salary
#Nycear Carroll
#11/21/2023
#use if/else to determine an employees pay


emp_name input('Enter employee name: ")
imp_hours inc(input("Enter employee hours: "))
emp_pay = foat(input("tner the empolyee input: "))

#Calulations
if emp_hours > 40:
    ot_hours = emp_hours - 40
    reg_hours = 40:

else:          #this represents if imp_hour is 40 or less
    ot_hours = 0
    reg_hours = emp_hours

#calulate pay
ot_pay = (emp_pay * 1.5) * ot_hours
ot_pay = emp_pay * reg_hours
gross_pay = ot_pay + reg_pay
