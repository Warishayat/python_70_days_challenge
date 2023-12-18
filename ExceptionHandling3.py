# Write a Python function that takes two numbers as input and returns their division.
# Handle the ZeroDivisionError and TypeError exceptions.



def division(a,b):
    try:
        return a/b

    except ZeroDivisionError:
        print("Cant divie some number with zero....")
    except TypeError:
        print("Here yoou make some tyoe error......")


num=int(input("Enter te number1:"))
num2=int(input("Enter te number2:"))

division(num,num2)




    