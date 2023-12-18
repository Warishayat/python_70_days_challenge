
# Create a program that asks the user to enter numbers 
# until they type "done." Handle both ValueError for 
# invalid inputs and a custom 
# StopIterationError if the user enters "stop."


while True:
    try:
        num=(input("Enter the number:"))
    
        if num.lower() == 'done':
            break
        else:
            print(num)
    except ValueError:
        print("Here we have value error:")