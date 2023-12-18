# Write a Python function that takes two numbers as input and returns their division.
# Handle the ZeroDivisionError and TypeError exceptions.
# def division(a,b):
#     try:
#         return a/b

#     except ZeroDivisionError:
#         print("Cant divie some number with zero....")
#     except TypeError:
#         print("Here yoou make some tyoe error......")


# num=int(input("Enter te number1:"))
# num2=int(input("Enter te number2:"))

# division(num,num2)



# Write a Python function that takes a number as input.
# Use a try-except block to handle ValueError.
# If the input is a valid integer, print the square of the number;
    
def squreNumber(num):
    try:
        num = int(num)
    except ValueError:
        print("Error: Please provide a valid integer.")
    else:
        result = num ** 2
        print(f"The square of {num} is: {result}")

n=int(input("Enter some number: "))
squreNumber(n)