#Question:Create two variables, x and y, and assign them integer values.
#Write a Python expression that evaluates to True if both x is greater than 5 and y is less than 10.




var_x=int(input("Enter a integer value:"))
var_y=int(input("Enter a integer value:"))


is_flag=True

if var_x > 5 and var_y > 5:
    print(is_flag)
else:
    is_flag=False
    print(is_flag)
