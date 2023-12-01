# Write a Python program for a library management system. 
# The program should simulate the process of checking out books. 
# It should consider the following conditions:
# The user can borrow a maximum of 5 books at a time.
# If the user wants to borrow more than 5 books, 
# they should receive a message stating they've exceeded the limit.
# If the user borrows fewer than or equal to 5 books:
# The program should ask the user for the number of books they want to borrow.
# For each book, ask for its title.
# Display a message confirming the books borrowed and their titles.
# Make sure the program handles cases where 
# the user enters invalid inputs, such as negative numbers
# or non-numeric input for the number of books



print("************************Welcome to Library Managment*******************")

B_Book=int(input("Enter the Number of Book you want to borrowed: "))

if B_Book>5:
    print("stating you've exceeded the limit: ")
else:
    Borrowed_Book=[]
    for i in range(1,B_Book+1):
        titlee=input("Enter the name of Book:")
        Borrowed_Book.append(titlee)

    #now for Displaying the book:

    print("Your borrowed total book=",B_Book)
    for i, titlee in enumerate(Borrowed_Book,start=1):
        print(f"{i}. {titlee}")


