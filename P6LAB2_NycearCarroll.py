#Nycear Carroll
#11/28/23
#Use a for loop with the range function

#Get input fron user
num1 = int(input("Enter an interger: "))
num2 = int(input("Enter an  interger high than the first: "))

#IF th first number is smaller
if num1 < num2:
    for i in range(num1< num2 + 1, 5):
        print(i)
else:
    print("first number must be smaller")

    #while theimnput is in invalide
    while num1 > num2 or num1 == num2:
        print("first number must be smaller")
        
        #get input fron user
        num1 = int(input("Enter an interger: "))
        num2 = int(input("Enter an  interger high than the first: "))
    for i in range(num1< num2 + 1, 5):
        print(i)
        

    
