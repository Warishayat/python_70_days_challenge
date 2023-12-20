#today we will cover the final keyword 
#try and excepthandle the error where final keyword use for cleanup.mean a thing 
#that we want to execute in every conditoin.


#example1

try:
 l=[1,2,3,4,5,6,7,8]
 n=int(input("Enter the index"))
 print(l[n])
except:
 print("Here we have index error")
finally:
    print("This line of code will be ececuted in every condtion")

#if we do the dame thing with function
def fun():
    try:
        l=[1,2,3,4,5,6,7,8]
        n=int(input("Enter the index"))
        print(l[n])
        return 1
    except:
        print("Here we have index error")
        return 0

    finally:
        print("This line of code will be ececuted in every condtion")
    
result=fun()
print("The value of result is",result)


# Write a Python program that reads a text file named "sample.txt" and prints the number of 
# lines in the file. If the file is not found, handle the exception and print an appropriate error message.

# Feel free to attempt these questions, and if you have any specific doubts or need help with solutions, feel free to ask!
try:
    with open("read.txt") as f:
    
        showoutput=f.readline()
        print(showoutput)
except FileNotFoundError:
       print("Your file is not in dbms system")
finally:
       print ("Everything is on track right now")