#SortHand_ifelse:
num=int(input("Enter the number: "))
num2=int(input("Enter the number: "))

print ("A is greater",num) if num > num2 else print("=") if num==num2 else print("B is greater",num2)


# Write a one-liner in Python that checks if a given number num is even or odd 
# and prints "Even" or "Odd" accordingly.
try:
    num1=int(input("Enter the number: "))

    print("NUmber is even:") if num1%2==0 else print("Number is odd")

except ValueError:
    print("You make some value error.")

# Write a one-liner in Python that determines if a given year year is a leap year and prints 
# "Leap year" or "Not a leap year" accordingly.

year=int(input("Enter the year: "))

print("leap year",year) if year%4==0 else print("Not a leap year",year)