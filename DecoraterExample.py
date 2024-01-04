# Your decorator implementation here
# Write a Python decorator repeat that takes an integer parameter n and repeats the
# execution of the decorated function n 
# times.

def repeat(n):
    def decorator(greet):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                greet(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    """Greet a person by name."""
    print(f"Hello, {name}!")

# Test the decorated function
greet("Alice")


#WE WILL GO BACK TO question and wwe make full code through this answer.
# Before function execution.
# The result is: 8
# After function execution.

def decorator(sum):
    def wrapper(*args,**kwargs):
        print("Before Function Execution.")
        sum(*args,**kwargs)
        print("After function executtion")
    return wrapper

@decorator
def sum(x,y):
    print("The result is:",x+y)


sum(4,4)


#magine you want to create a special tool in Python that measures 
# how much time a certain task takes to finish. For example, if you
# have a function that adds two numbers, you want to know how long it 
# takes to do that addition.
# Your task is to create this tool, called a 'decorator,' 
# which you can attach to any function to measure its time. After 
# creating this tool, apply it to a simple function, like adding two numbers
# , and show how it works.


import time

def decorator(taskperfoamne):
    def wrapper(*args):
        print("Your task is in execution form.")
        taskperfoamne(*args)
        print("Your task is executed succesfully.")
    return wrapper



@decorator
def taskperfoamne(result):
    print("Your task take",result)
          
result=time.ctime()
print(result)
taskperfoamne(result)