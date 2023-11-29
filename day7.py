#Day 7/70 i will cover the Elif contol statment:
# we will further categeroised the example of day 6/70 challenge problem.

cost_price=int(input('Enter the cost price of the item:- '))
sell_price=int(input('Enter the sell price of the item:- '))

if cost_price>sell_price:           #if cost price is higher the selling
    loss=cost_price-sell_price
    print('You sell the item in low price you made the loss of rs=',loss)
elif sell_price>cost_price:           #elif sell price is higher the Cost
    profit=sell_price-cost_price
    print('Congrats You sell the item with profit rs=',profit)
else:                                #if sell price is equal the Cost price
    print("You make no profit no loss :-) ")