#Ternanry operator:(last conditional operator)
#Simplify the content with in one ine of code.
#Question: Write a program to check if number is odd or even using ternery operator:

number1=int(input("Enter the number"))
output="even" if number1%2==0 else "odd"
print("The output is ",output)

#take two number from the user and tell which one is maximum using ternery operator>

num1=int(input("Enter the number1: "))
num2=int(input("Enter the number2: "))

result ="Num1 is maximum:" if num1>num2 else "Num2 is greater:"

print(result)

#write a program that determine the absolute value of a number.using ternery operator?
n1=int(input("Enter a number: "))
ternery=n1*(-1) if n1<0 else n1
print("Absolute value is: ",ternery)


#Write a progra to check  if a person is above the eighteen then he/she will be eligible for the vote oher wise iyt should return you are not eligible:

age=int(input("Enter your age:-"))

check_ternery= "yOu are eligible for vote " if age >= 18 else " Sorry You are not eligible for vote "

print(check_ternery)