#Todays 3/70 day challenge and i would cover the diffrent datatypes of python
#Numeric data types = int(100,256 etc) ,float (1.1 2.5 etc) and complex (real and imaginary 60+25j) data tyes.
#Sequence = list([1,2,3] unique and modifiable) ,tuple (1,2,3)(it can be duplicate and canot be modifiable) and string--> used for sequence of same data.
#mapping data type= dictionary (key value pair like student{name :waris,rollno:sp21368}) where student is the variable of dictionary its enclosed by curly bracket.
#Set data types= collection of unique item e.g={"apple",'banana','orange'}
#none=nothing which gave us null value
#ASCII = AMERCIAN standard code for interchange ehich help to reprsent chracter as numeric code. eg: A TO Z are numeric values from 65 to 90.small letter a toz from 97 to 122.
#check inbuilt module of ascii and numeric


char ="a"
print (ord(char))                       #inbuilt to check the numeric from ascii 
ascii =67
print(chr(ascii))                       #inbuilt function to check ascii from numeric


#taking input from the user

name= input("Enter the name:-")   #input always captured in string
print(f"your name is: {name}") 
print (type(name))

#typecasting is used to convert the one data type  to another.
age =int (input("Ënter you age:-"))
print(f"your age is:- {age}")