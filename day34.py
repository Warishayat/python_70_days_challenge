#today i will cover the local and global variable:

x=10 #global variable


def welcome():
    global x
    y=20   #now it will change the value of x from 10 to 12.
    #local variable which can not acess outside from he class but inside the class
 
    print(y)    # if we want to change global variable
#we can access the loca variable with in the function only

    
welcome()
print(x)

# print(y)=====> it will throw error because we call it outside from the function
