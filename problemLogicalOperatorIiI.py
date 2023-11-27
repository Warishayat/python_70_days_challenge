#Question:Take two user inputs, num1 and num2, both integers.
#Write a Python script that prints "Both numbers are even" if both num1 and num2 are even numbers, "Both numbers are odd" if both are odd, and "Mixed parity" otherwise.
num1=int(input("Enter a num1 value:"))
num2=int(input("Enter a num2 value:"))

if num1 % 2==0 and num2 % 2==0:
    print("Both Number are Even:- ")
elif num1 % 2 !=0  and num2 % 2 !=0:
    print("Both Number are Odd:- ")
else:
    print("Both Number Mixed Parity:-")
