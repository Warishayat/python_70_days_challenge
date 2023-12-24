#if __name__=="__main__"???????
#__name__ it basically tell us from where we are going to execute our file.
#if this file is going to be excecued from main then print welcome other wise leave that.

def greet():
    print("Hello waris")
if __name__=="main":
    print(__name__)
    greet()


from Namemain import some_function

print(some_function())


#explanation
# What is the purpose of if __name__ == "__main__": in Python?

# Answer:

# The if __name__ == "__main__": statement is used to determine whether
# the Python script is being run directly or if it is being imported as
# a module into another script. The code block following this statement 
# is executed only when the script is run directly.