#decorater which take the function and return the function.

def greet(fx):
    def mfx():
        print("Good morning")
        fx()
        print("Thanks for using this function")
    return mfx



@greet
def add(a=12,b=13):
    print("The answer is",a+b)
add()



# #example2
# Write a Python decorator authenticate that simulates a simple 
# authentication mechanism. The decorator should prompt the user for
# a password, and if the correct password is entered, the decorated function
# is executed; otherwise, an authentication failure message is printed.


# setpassword='abbasi123'

# def authenticate(authentication):
#     def mfx():
#         num=input("Ënter Password:")
#         if num==setpassword:
#             print("Succesfull")
#             authentication()
#         else:
#             print("Authentication failuer")
#     return mfx      
    


# @authenticate
# def authentication():
#     print("Password exectued succesfully:")


# authentication()