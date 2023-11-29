#QUESTION: if cost and selling price of the item enter through the keyboard.write a program\nto determinewether the seller has made profit or loss or no profit no loss.Also determine how much profit or loss he incurred?
#its the part of the if else loop.


cost_price=int(input('Enter the cost price of the item:- '))
sell_price=int(input('Enter the sell price of the item:- '))

if cost_price>sell_price:           #if cost price is higher the selling
    loss=cost_price-sell_price
    print('You sell the item in low price you made the loss of rs=',loss)
if sell_price>cost_price:           #if sell price is higher the Cost
    profit=sell_price-cost_price
    print('Congrats You sell the item with profit rs=',profit)
else:                                #if sell price is equal the Cost price
    print("You make no profit no loss :-) ")