#Print the ascii value a to z

for i in range(67,91,1):
    print(chr(i))   #Capital A to Z

for i in range(97,123,1):
    print(chr(i))  #Small a to z


#solve a problem take a input from the user and find the factorial of input users?

user=int(input("Enter the Number for find the factorial:"))
factorial =1

while(user>0):
    factorial=factorial*user
    user-=1 
 
print("The Factorial is",factorial)

#calculate and print the fabonacii series:

list=[0,1]   #011235
n=10
for i in range(2,n):
    thirdNumber=list[i-1]+list[i-2]
    list.append(thirdNumber)
print(list)

#do the smae code without list

n1=0
n2=1
n3=10
for i in range(2,n):
    n3=n2+i
print(n1,n2,n3,end ="")
