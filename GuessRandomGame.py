#Q1:(while_loop) write a program that count the numbers of digits in a given intergers?
n=int(input("Enter range:-"))

count=0
while (n!=0):
    n//=10
    count+=1
print(count)

#Question2: check the number is palindrome or not?
number=input("Enter a number:")

Cpalindrome=number[::-1]

while True:
    if number==Cpalindrome:
        print("the number is palindrome")
        break
    else:
        print("the number is not palindrome")
        break


#Q3:implement a program  that ask the user to guess a random number and provide the deedbac its high or low?

import random as round
while True:
    rando=round.randint(1,100)

    guess=int(input("Enter the guess the number between 1 and 100 :- "))

    if guess==rando:
        print("you guess is equal to computer guess:")
        print("Your guess number is:",guess)
        print("Computer guess number is:",rando)
    elif guess<rando:
        print("Alas! your guess number is low:")
        print("Your guess number is:",guess)
        print("Computer guess number is:",rando)
    else:
        print("Alas! your guess number is to high:")
        print("Your guess number is:",guess)
        print("Computer guess number is:",rando)

    enquirey=input("Do you want to continue or brake: (y/n)")

    if enquirey !="y":
        break




