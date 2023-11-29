# Write a Python program that takes a temperature as input and classifies it as "low," "medium," or "high." Use if, elif, and else statements to implement the classification based on the following criteria:
# Low: Temperature below 0 degrees Celsius
# Medium: Temperature between 0 and 25 degrees Celsius (inclusive)
# High: Temperature above 25 degrees Celsius.

temp=float(input("Enter the temprature of you area:- "))


if temp <= 0 :
    print("Temprature is low:")
elif temp <=25:
    print("Temprature is Medium: ")
else:
    print("Temp is High:")
    


