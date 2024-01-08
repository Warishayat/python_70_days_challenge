#today i will solve a exercise by using oop concepts:
#exercise requiremnts:
# define a class with the library name  with some variables no of books and Books(which)
#will be list,no of books will tell us about the total book in the list if the no of books 
#is less then or greater then you enterd or from the books list:make method that will tell
#no of book are equal to len of book if not that will tell theres is some problem.
  
class library:
    def __init__(self):
        self.no_of_book=0
        self.Book=[]

    def Total_Book(self):
        print("Total no of book you enterd",self.no_of_book)
        print("The Total Book in the List:",self.Book)
    def Addbook(self):
        name=input("Enter the Book name you wan to add:").strip()
        Book_name=name.replace(" ", "")
        print("The Book that you want to add:",Book_name)
        if Book_name.isalpha():
            self.Book.append(Book_name)
            self.no_of_book +=1
            print("Book is succesfully added to list")
            print("Total Book you added:",self.no_of_book)
            print("Your Book List:\n",self.Book)
        else:
            print("You enter some thing invalid:")
    def DeletBook(self):
        print(self.Book)
        
        idx=int(input("Enter the number that you want to delet 0 for first Book 2 for next and so on...:"))
        self.Book=self.Book.pop(idx)
        self.no_of_book -=1
        print("Item delet Successfully:")
        
person=library()
while (True): 
    try:
        num=int(input("""Enter your choice:
        1: for Total_Book
        2: for Add_Book 
        3: for Delet_Book \n
        """))
    except ValueError:
        print("You make ValueError")
    if num==1:
        person.Total_Book()
    elif num==2:
        person.Addbook()
    elif num==3:
        person.DeletBook()
    else:
        print("Wrong number choosen.")

    StartEnd=input("Stay or leave the app only (y/or any key to break)").lower()
    if StartEnd != 'y':
        break
    else:
        pass