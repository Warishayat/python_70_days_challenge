# Write a Python program that checks if a given year is a leap year. 
# A leap year is either divisible by 4 but not divisible by 100 unless it is divisible by 400. Use if, elif, 
# and else statements to implement the logic and prompt the user for input.
year=int(input("ENter the year: "))

if (year % 4 == 0 and year % 100 !=0) or (year % 4==0):
    print("The year is Leap year:")
elif year % 100 != 0:
    print("This year is not a Leap year.")

