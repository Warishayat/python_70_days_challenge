# Write a lambda function to calculate the square of a given number.
# Use this lambda function to find the square 
# of the number 7.
calculate_squre= lambda x: x**2 

#we will call lambda function and pass the value for x

print("The answer is:",calculate_squre(7)) #answer should be 49

# 2: Create a lambda function that takes two parameters and returns
# their sum. Use this lambda function
# to add the numbers 10 and 20.
Sumvalue= ( lambda x,y: x+y)

result=Sumvalue(10,20)
print(f"The value of sum of both number is=",result)



# Write a lambda function to check if a given number is 
# even. Use this lambda function to check 
# whether the number 15 is even or not.

is_odd=lambda x:True if x % 2 != 0 else False

result=is_odd(15)

print(f"{15} Number is",result)


# Create a lambda function that takes three parameters (x, y, z) and
# returns the sum of the squares of these parameters.

ThreeSumSqure = lambda x,y,z: x**2+y**2+z**2

final_result=ThreeSumSqure(12,13,14)

print("The final result is",final_result)

# Create a lambda function that takes two strings and concatenates them.
# Use this lambda function to concatenate
# the strings "Hello" and "World".


Concate_string=lambda h,w: h+w
h="Hellow "
w="World"
final=Concate_string(h,w)
print(final)
# 
# Write a lambda function to calculate the exponentiation of two 
# numbers (a to the power of b). Use this lambda function to find the
# result of 
# 2
# 3
# 2 
# 3






    







