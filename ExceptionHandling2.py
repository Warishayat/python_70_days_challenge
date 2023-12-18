# Create a function that takes a list and an index as input and returns the element at that index.
# Handle both IndexError and TypeError gracefully.
def fuc(liist,num):
    try:
        result=liist[num]
        return result
    except IndexError:
        print("Index error found ",IndentationError)

liist=[1,11,122,133,1341,15,145]
try:
    num=int(input("Enter te number:"))

    result=fuc(liist,num)
    print("The element at that index is:",result)
except TypeError:
    print("Type error found:",TypeError)
except ValueError:
    print("ValueError found:",ValueError)