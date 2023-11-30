#Question: take a positive integer number and tell its four digit number or not.?

number=int(input("Enter the number:-"))

#number should be lies between 1000 and 9999 the that will be four digit number>

if number>=1000 and number<=9999:
    print("Enterd number is Four digit Number:-")

elif number>=100 or number<=999:
    print("your number is between 1 and 3 digit:-")
else:
    print("Your enterd Number is greater than four digit:- Thanks")