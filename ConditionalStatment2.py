#Question:Leap Year Checker:
#Create a program that checks whether a given year is a leap year or not. Allow the user to input the year.


#leap year are those they have 53 weeks in a year and leap year are those which devide completley with 4:

year=int(input("Enter the year that you want to check:- "))

if year % 4  == 0:
    print("The year is leap year:")
else:
    print("The year is not year:")