# Write a function called calculate_total 
# that takes two positional arguments, price and quantity,
# and returns the total cost by
# multiplying them. Test the function with different values

def calculate_total(price ,quantity):

    return price*quantity

total_cost=calculate_total(30,3)
print("The total cost is:",total_cost)

# Define a function greet_user that takes two arguments 
# - name and greeting (with a default value of "Hello"). 
# The function should print a personalized greeting message.
# Test the function by calling it with different values for 
# name and using the default greeting.

def greet_user(name,greeting="Hellow"):
    print("",greeting,"",name)

greet_user(name="waris")


# Write a function calculate_sum that accepts a variable number of arguments
# and returns the sum of all the arguments. Test the function with 
# different numbers of arguments.

# Hint: Use the *args syntax.

def calculate_sum(*numbers):
    sum1=0
    for i in numbers:
        print(i)
        sum1=sum1+i
    return sum1

total=calculate_sum(12,15,16,56,70)
print("Total sum is",total)


