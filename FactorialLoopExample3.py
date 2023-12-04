# Factorial Calculation:
# Write a program to calculate the factorial of a given number using a while loop.
num=int(input("Enter the number for factorial:"))

fact=1

while(num>1):
    fact=num*fact
    num-=1
print("factorial of given number is:",fact)

