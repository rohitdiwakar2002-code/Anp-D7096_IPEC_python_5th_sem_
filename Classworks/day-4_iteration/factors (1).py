<<<<<<< HEAD
''' Program to display factors of the given number'''
#input of number from user
num = int(input("Enter any number : "))
#------------------------------------------
if(num == 0 ):
    print("Infinite Factors")
elif(num > 0):
    #positive number
    print("Factors are : ")
    for x in range(1,num + 1):
        #to check divisibility of num by x
        if(num % x == 0):
            print(x,end =',')
else:
    #negative number
    number = -num
    print("factors are : ")
    for x in range(1,number + 1):
        if(num % x == 0):
=======
''' Program to display factors of the given number'''
#input of number from user
num = int(input("Enter any number : "))
#------------------------------------------
if(num == 0 ):
    print("Infinite Factors")
elif(num > 0):
    #positive number
    print("Factors are : ")
    for x in range(1,num + 1):
        #to check divisibility of num by x
        if(num % x == 0):
            print(x,end =',')
else:
    #negative number
    number = -num
    print("factors are : ")
    for x in range(1,number + 1):
        if(num % x == 0):
>>>>>>> 1a114127dd04c6b139aa2f4bc8f9ea61b8b80e89
            print(x, ",", -x ,end=',')