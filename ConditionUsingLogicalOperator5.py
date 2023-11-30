#Question: Take 3 integer and print the greatest of them:

num1=int(input("Enter the Number 1 :-"))
num2=int(input("Enter the Number 2 :-"))
num3=int(input("Enter the Number 3 :-"))


if num1>num2 and num2>num3:
    print("The most greatest number is num1:",num1)
elif num2>num3 and num3>num1:
    print("The most greatest number is num2:",num2)
else:
    print("The most greatest number is num3:",num3)
