#conditional statment: it same work like switch case.
#we choose answer on the basic of condition its only supported in python 3.10 version
#we will try to make calcualtor.


num1=float(input("Enter the number1:- "))
num2=float(input("Enter the number1:- "))

operator=input('''
1 for plus the number:
2 for subtract the number:
3 for divide the number:
4 for multiply the number:
5 for modulous the number:
6 for exponent the number:
7 for floor division number:
''')

match operator:
    case '1':
        print("The plus of num1 and num2 is: ", num1+num2)
    case '2':
        print("The subtraction of num1 and num2 is: ", num1-num2)
    case '3':
        print("The division of num1 and num2 is: ", num1/num2)
    case '4':
        print("The multiplication of num1 and num2 is: ", num1*num2)
    case '5':
        print("The modulus of num1 and num2 is: ", num1%num2)
    case '6':
        print("The exponent of num1 and num2 is: ", num1**num2)
    case '7':
        print("The fllor division of num1 and num2 is: ", num1//num2)
    case _:
        print("You have enterd some invalid value :-)")