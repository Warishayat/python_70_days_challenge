# #in tosday class we will try to cover the file handling in python...
with open('myfile.txt','a') as f:   #write method
    f.write("Python is easy")
    f.write("Welcome to the file handling:\n")
    f.write("Welcome to the waris channel:\n\n")
    f.write("Welcome to the file:\n")



# #now we will cover the writeline() method:
lis=['welcome\n''to\n','Waris\n','challenge\n']

fileopen=open("myfile.txt",mode='a+',encoding='utf-8')
fileopen.writelines(lis)
fileopen.close()

# #new file to enter the data
fruit=['banana\n','apple\n','avacado\n','mango\n']
vagitables=['adyfinger\n','onion\n','patato\n','ginger\n']
wear=['shirt\n','pants\n','jacket\n','cap\n']
f=open("file1.txt",'a')
f.writelines(fruit)
f.writelines(wear)
f.writelines(vagitables)
f.write("Append all these thigat he end of the code")
f.close()



# Openfile to eard the data
filee=open("file1.txt",'r')
result=filee.read()
print(result)
filee.close()

#readline and readlines()
#readline

with open("file1.txt",'r') as f:
    result=f.readlines()
    print(result)

# Write a Python program that accepts user input to create a file.
# Allow the user to enter multiple lines of text. Save the input to 
# a file named "user_data.txt". Handle potential errors during file
# operations.
str=input("Enter a string")
result=open("filee.txt",'w')
result.write(str)
result.close()

# You are given a text file named "input.txt" that contains 
# a list of numbers, one per line. Each line may have an integer
# or a floating-point number. Your task is to read the file,
# calculate the sum of all the numbers, and write the result to 
# a new file named "output.txt" in the following format:
with open ("input.txt",'r') as f:
    print(f.write())
    

