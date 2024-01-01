#today i will solve the exercise of snake waiter and gun game:
import random as rd 


def GameStart(computerchoice,userchoice):
        # 0 return in case of computer win
        # 1 return in case of user win
        # 2 return in case of draw the match
    if userchoice==computerchoice:
            return 2
    elif userchoice == 1 and computerchoice== 3:
                return 0
    elif userchoice==2 and computerchoice==1:
            return 0
    elif userchoice==3 and computerchoice==2:
            return 0
    else:
            return 1
        
while True:
        

    userchoice=int(input("""
    choose the number:
    1: for snake
    2: for water 
    3: for gun: \n"""))
    computerchoice=rd.randint(1,3) 
    if userchoice>=1 and userchoice<=3:
        result=GameStart(computerchoice,userchoice)
    else:
        print("Choose the number between 1 and 3:")
        continue
    

    if result==2:
        print("Match is draw")
        print("Your choice was:",userchoice)
        print("Computer choice is:",computerchoice)
        break
    elif result==1:
        print("Congratulation you win from the computer:")
        print("Your choice was:",userchoice)
        print("Computer choice is:",computerchoice)
    else:
        print("Alas! You loose from the computer:")
        print("Your choice was:",userchoice)
        print("Computer choice is:",computerchoice)
