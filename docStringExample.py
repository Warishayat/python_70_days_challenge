#doc_stringExample

def is_prime(num):
    '''Here we will pass a number by calling function through main if the number that will
    gave us true other wise it gave us fall.
    '''
    if num<0:
        raise ValueError("You enter negative number")
    elif num==1:
        return False
    elif num==2:
        return True
    else:
        for i in range(2,num):
            if num % i != 0 :
                return True
            else:
                return False
                
            

number=int(input("Enter the number: "))
result=is_prime(number)
print("Result is =",result)
