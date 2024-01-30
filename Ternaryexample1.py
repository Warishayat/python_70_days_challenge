# Write a Python program that takes a temperature 
# in Celsius as input and uses a ternary operator to conver
# t it to Fahrenheit. Output the result.

celcius=float(input("Enter the temprature in celcius:"))
Fahrenheit=(celcius*1.8)+32 
print(f"The temp is",Fahrenheit)
              


# Given a student's score as input, use a ternary operator to 
# classify the student's grade. Assume the grading scale is A (90-100), 
# B (80-89), C (70-79), D (60-69), and F (0-59).

marks=int(input("Enter the marks:"))
result='a' if marks>=90 else "b" if marks >=80 and marks<90 else 'c' if marks>=70 and marks<79 else 'd' if marks>=60 and marks <69 else 'f' 
print("Your result grade is:",result)

# Write a Python function that takes two numbers as input 
# and uses a ternary operator to calculate
# and return the absolute difference between them.

def tern(a,b):
    cal=a-b if a>b else b-a
    return cal
n1=int(input("Enter the number1:"))
n2=int(input("Enter the number1:"))
a=tern(n1,n2)
print("The diffrence is:",a)



# Write a Python function that takes a string as input and
# uses a ternary operator to determine if the string is a 
# palindrome. Return True if it is, and False otherwise.

userinput=input("Enter the string:")

result=True if userinput[::-1]==userinput else False
print("Is_palindrome:",result )