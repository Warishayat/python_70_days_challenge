#Today i will cover the error handling /exception handeling....

#if the number is divided by zero.then it will raise zero division error.
try:
    num =int(input("Enter the number:"))
    num2=int(input("Enter the number two:"))

    answer= num/num2
    print(answer)
except ZeroDivisionError:               #this caught zero divsion error.
    print(ZeroDivisionError)

print("Program continously working using track")

print()

# Create a function that takes a list and an index as input and returns the element at that index.
# Handle both IndexError and TypeError gracefully.
try:
    lst=[1,2,3,4,5,6,7,8]
    num=int(input("Enter the index number:"))
    result=lst[num]
    print("The result at this index is ",result)
except IndexError:
    print("Error 404 found!")
except TypeError:
    print("305! type error occured.")
except ValueError:
    print("409! value error found.")

    
try:
    num=input("Enter the number:")
    num2=int(input("Enter the number:"))

    print(num+num2)
except TypeError:    
    print("Here is a type error")

print("Hellow here we have value error")


#ValueError:
try:
    num=int(input("Enter the number:"))
except IndentationError:
    print("Here you do some valuerror.")



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

    
# Create a function that takes a list and an index as input and returns the element at that index.
# Handle both IndexError and TypeError gracefully.
def fuc(liist,num):
    try:
        result=liist[num]
        return result
    except IndexError:
        print("Index error found ",IndentationError)
 

liist=[1,11,122,133,1341,15,145]
try:
    num=int(input("Enter te number:"))

    result=fuc(liist,num)
    print("The element at that index is:",result)
except TypeError:
    print("Type error found:",TypeError)
except ValueError:
    print("ValueError found:",ValueError)