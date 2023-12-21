# 1: Minimum of Two Numbers:
# Write a one-liner to find and print the minimum of two numbers (a and b) 
# using the shorthand if-else statement.

a=10
b=6

print("A is greater") if a > b else print("B is Greater")


# 2: Even or Odd:
# Create a short program that takes an integer as input and prints "Even" if it's even and "Odd" if it's odd, 
# using the shorthand if-else statement.

num=int(input("Enter the number:"))
print(f"{num} is even") if num%2==0 else print (f"{num} is odd")

# 3:Write a one-liner to calculate and print the absolute value of a 
# given number using the shorthand if-else statement.

n=-12
print("The number is absoulte") if n>0 else print("Number is not absoulte")


# 4:Write a one-liner to assign a letter grade (A, B, C, D, or F)
# based on a numeric score (score), using the shorthand if-else statement

marks=int(input("Enter the marks:"))

print("The grade is A:") if marks>=80 else print("The grade is B:") if marks>=70 else print("The Grade is C") if marks>=60 else print("The Grade is D:" if marks >=50 else print("You acheive Grade F try again!"))