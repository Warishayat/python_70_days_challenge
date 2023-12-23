while True:
    import random as rd

    def guessnumber(cchoice,num):
        if num < 0 or num > 11:
            print("Choose the number between 1 and 10:")
        else:
         #call the function
            if num==cchoice:
                
                print("You Guess right.")
                print("You choose.",num)
                print("Computer choose.",cchoice)
                
            if num<cchoice:
                print("Your Guess number is low:",num)
                print("Computer Choice number is:",cchoice)
            if num>cchoice:
                print("Your guess Number is high:",num)
                print("Computer  number is:",cchoice)
        
    cchoice=rd.randint(1,10)
    num=int(input("Enter the guess number between 1 & 10:"))
    #call the function:
    guessnumber(cchoice,num)
   
    if num==cchoice:
        break
8