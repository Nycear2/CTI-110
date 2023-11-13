#A bref description of this project
#1/9/2023
#CTI-110 P1HW2 - Travel Expense
#Nycear J. Carroll
#

User_budget = int(input("Input User budget: "))
Location = int(input("input User location: "))
Asset_into_gas = int(input("input Gas Spending: "))
Asset_into_accommodation = int(input("input Accommodation spending: "))
Asset_into_food = int(input("input Food Spending: "))
Remaining_balance = User_budget - Location - Asset_into_gas - Asset_into_accommodation - Asset_into_food

print("-----------Travel Expenses------------")
print("Location: ", Location)
print("User budget: ",User_budget)
print("Asset into gas: ",Asset_into_gas)
print("Asset into accommodation: ", Asset_into_accommodation)
print("Asset into food: ", Asset_into_food)
print("Remaining balance: ",Remaining_balance)
