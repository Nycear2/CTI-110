#Nycear j. Carroll
#11/14/23
#use float vaule to represent the coast of drive a specified distance 

#Get unput from user
mpg = float(input("Enter miles per gallon as decimal: "))
cost_gal = float(input("Enter the coast for one gallon of gas: "))

#Calcuate coast to drive 20 miles
drive_cost_20 = (20/mpg) * cost_gal

#Calcuate coast to drive 75 miles
drive_cost_75 = (75/mpg) * cost_gal

#Calcuate coast to drive 500 miles
drive_cost_500 = (500/mpg) * cost_gal

#Output th coast with two decimal places using a f-string 
print(drive_cost_20)
print(f"cost to drive 20 miles is {drive_cost_20:.2f}")
print(drive_cost_75)
print(f"cost to drive 75 miles is {drive_cost_75:.2f}")
print(drive_cost_500)
print(f"cost to drive 500 miles is {drive_cost_500:.2f}")
