#Question:Grading System:
#Write a Python program that takes a student's score as input and prints the corresponding grade. Use the following grading scale: A (90-100), B (80-89), C (70-79), D (60-69), F (0-59)?

marks=int(input("Enter the marks:- "))

if marks>=90 and marks <=100:
    print("CONGRAGULATE!! you got Grade A:- ")
elif marks>=80:
    print("CONGRAGULATE!! you got Grade B:- ")
elif marks>=70:
    print("CONGRAGULATE!! you got Grade C:- ")
elif marks>=60:
    print("CONGRAGULATE!! you got Grade D:- ")
else:
    print("ALAS!!!!!!! you got Grade F mean Fail:- ")