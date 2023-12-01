#Question: Write a program to determine the categeory of a product base on its price.using nested if-else statment.
#price between---->50 output "Budget"
#price between---->50 and 100 output "Mid Range"
#price between---->101 and 200 output "Premium"
#price greater than---->200 output "luxury"


price=int(input("Enter the price:- "))

if price<50:
    print("Budget")
else:
    if price<=100:
        print("Mid Range")
    else:
        if price <=200:
            print("Premium") 
        else:
            print("Luxury")

###take a year value from the user and tell it's leap year or not:

year=int(input("Enter the year:- "))


if year%4==0:
    print("The year is leap year: ")
else:
    print("Year is not leap year: ")