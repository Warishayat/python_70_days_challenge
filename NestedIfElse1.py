#Question: Take the positive integer and tell its divisible by 3 or 5 but not by 15.

num=int(input("Enter the number:- "))

if num % 15 == 0:
    print("Number is divisible by 15:-")
else:
    if num%3==0  or num % 5==0:
        print("Number is not divisble by 15 but with with 3 and 5")
    else:
        print("Neither divisble by 3 or 5")