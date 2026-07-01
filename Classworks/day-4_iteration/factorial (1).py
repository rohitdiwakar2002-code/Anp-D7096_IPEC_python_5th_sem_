'''Program to calculate factorial of a number'''
#input of number from the user
num = int(input("Enter any number : "))
#---------------------------------------
if(num < 0):
    #negative number
    print("Factorial not possible")
elif(num == 0):
    print("Factorial = 1 ")
else:
    #positive
    fact = 1
    for x in range(1,num + 1):
        fact = fact * x
    #--------------------------
    print("factorial = ",fact)