#Doc_.string



def avg(a,b):
    '''here our code will sum of the number and return the avg 
    to the main.
    this is the simplest way of doc string.its just like comment but comment is 
    dffrent comment cannot change ourr code imoact but it can change'''
    
    return a+b/2

n=avg(12,13)
print("The avg is:",n)
print(avg.__doc__)



#practise question 
def calculate_rectangle_area(length, width):
    '''Here our code will take the length and width through the function
    and return the value of that function through with the return value
    '''

    if length < 0 or width < 0:
        raise ValueError("Hellow here you have some valueError.")
    return length*width
    
length=int(input("Enter the length of the function:"))
width=int(input("Enter the width of the function:"))

final_result=calculate_rectangle_area(length,width)
print("The result is:",final_result)
print(calculate_rectangle_area.__doc__)