#Question: Write a program that take the total purchase amount as input and output the corresponding discount percentage:
#100$ ----> 20% discount
#55 to 99$ ------>10%
#below------>No discount

purchase_amount=int(input("Enter the total amount of purchasing:- "))

if purchase_amount>=100:
    print("Congragulation you will get the 20 percent discount:-")
    discount=purchase_amount/100*20
    purchase_amount=purchase_amount-discount
    print("NOW! your total amount is USDT=",purchase_amount)
    print("you get the discount of USDT=",discount)
elif purchase_amount>=55 and purchase_amount<=99:
    print("Congragulation you will get the 10 percent discount:-")
    discount=purchase_amount/100*10
    purchase_amount=purchase_amount-discount
    print("NOW! your total amount is USDT=",purchase_amount)
    print("NOW! you get the discount of USDT=",discount)
else:
    print("Below 55$ shopping there's no any discount :-)")

