#Day 9/70 --> Nested if else: for complex disicon making:a statment with in statment
#Question: Write a program that take the total purchase amount as input and output the corresponding discount percentage:
#100$ ----> 20% discount
#55 to 99$ ------>10%
#below------>No discoun
#dO Same code which i laready had done in python day 8. now do it wirth nested if else>

number1=int(input("Enter the Number1 :- "))
number2=int(input("Enter the Number2 :- "))
number3=int(input("Enter the Number3 :- "))

if number1>number2:
    if number1>number3:
        print("number1 is greatest all of them:- ",number1)
    else :
        print("number3 is greatest all of them:- ",number3)
else:
        if number2>number3:
            print("number2 is greater:- ",number2)
        else:
            print("number3 is greater all of them:- ",number3)

