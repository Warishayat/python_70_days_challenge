#Ask user to enter the number aand tell him its prime or not:
number1=int(input("Enter the number:- "))

if number1==1:
    print("Number is not prime: ")
else:
    for i in range (2, number1+1):
        if number1 % i == 0:
            print("The Number is not prime :-",i)
            break

            
        else:
            print("The Number is prime :-")
            break