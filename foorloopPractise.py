#for loop practuse question
#Question1:write a program to sum of all number in a given list?
list=[1,2,3,4,5,6,7,8,9,10]

sum=0

for i in list:
    sum=sum+i
    
print("The sum of al number of the list is=", sum )

#Question2: create a program that print the fabonacii series upto given number?

list=[0,1]
n=10


for i in range(2,n):
    third=list[i-1]+list[i-2]
    list.append(third)

print(list)




#Question3:impement a program that find and print all prime number less then equal to a given number?
startvalue=int(input("Enter the starting value: "))
endvalue=int(input("Enter the end value: "))

for i in range(startvalue,endvalue):
    if startvalue==1 and endvalue==1:
        print("number is not prime sorry")
    else:
        if i%2==0:
            print("Number are not prime:")
        else:
            print("Numbers are prime:",i)