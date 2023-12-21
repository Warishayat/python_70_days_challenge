# # 1:Maximum of Three Numbers:
# # Create a short program that takes three numbers (a, b, and c) as input 
# # and prints the maximum of the three using the shorthand if-else statement.

# a=int(input("Enter the num a:"))
# b=int(input("Enter the num b:"))
# c=int(input("Enter the num c:"))

# print("A is greater:") if a>b and a>c else print("B is greater:") if b>c and c>a else print("C is greater:")


# #2:Write a one-liner to check and print whether a given string is a
# # palindrome (reads the same backward as forward) using the shorthand
# # if-else statement.

# Str=input("Enter something to check palindrome:")
# palindrome=Str[::-1]
# print("This is palindrome:") if Str==palindrome else print("Not palindorme Sorry")


# #3: Create a program that takes a number as input and prints 
# # "Positive," "Negative," or "Zero" using the shorthand if-else statement.
# Input=int(input("Enter some number:"))
# print("Number is zero") if Input==0 else print("Number is positive:") if Input>0 else print("Negative number:")


# #4: Write a one-liner to check and print whether a given number is prime 
# # or not using the shorthand if-else statement.


isEven=int(input("Enter a number:"))
print("Number is even:") if isEven%2==0 else print("Number is odd:")