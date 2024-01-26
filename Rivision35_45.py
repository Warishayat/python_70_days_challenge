#Today rivison is from day 3 to day 45.
# def greet():
#     print("This function do welcome to he every body:")
#     print("Luv you all guys")
# print(__name__)
# if __name__=="__main__":
#     greet()
# # The code mentioned below is assume that in another file   
# import Welcome
# Welcome.greet()

# #Question 2
# def sum(a,b):
#     sum=a+b
#     print("The result of the sum is:",sum)
    
# if __name__=="__main__":
#     sum(12,13)

# #IMAGINE : the code mention below is in another file and its import a welcome module.
# import Welcome
# Welcome.sum(12,14)


#Os Module
#current working directory
# import os
# result=os.getcwd()
# print(result)

# #To make new directory
# direc="waris.txt"
# parent_directory="C:\\Users\\Waris Hayyat\\Desktop\\python\\waris.txt"
# result=os.path.join(direc,parent_directory)
# print("Sucessfuly created")
# os.mkdir(result)
# print("Directory '% s' created" % direc)

# #to delet the directory 
# import os
# file="waris.txt"
# path="C://Users//Waris Hayyat//Desktop//python"
# result=os.path.join(path,file)
# os.rmdir(result)
# print("The directory has been suceesfully deleted:")

# #to create multiple file 

# import os

# # Correct path to the directory (without the filename)
# path = "C:\\Users\\Waris Hayyat\\Desktop\\python"

# # Create the directory if it doesn't exist
# if not os.path.exists(path):
#     os.makedirs(path)

# # Use the correct path when creating files
# for i in range(1, 101):
#     file_name = f"python{i}.py"
#     file_path = os.path.join(path, file_name)

#     try:
#         with open(file_path, "w") as f:
#             pass  # Create empty file
#         print(f"Empty file {file_name} successfully created in {path}.")
#     except Exception as e:
#         print(f"Error creating file: {e}")

#now remove file
# import os
# path="C:\\Users\\Waris Hayyat\\Desktop\\python"
# for i in range(1,101):
#     file_name=f"python1.py"
#     path=os.path.join(path,file_name)
#     os.remove(path)

#file handling(in write mode)
# line="hellow my name is waris hayat abbasi i am enthusiat for \n for data science \n i wana work as a google developer"
# get=open("file.txt","w")
# get.writelines("Hellow this is my first program")
# get.writelines(line)
# get.close()
# print("file sucessfulyy run")

# #in read mode
# file=open("file.txt","r")
# get_read=file.readline()
# print(get_read)
# file.close()

#in append mode
# with open ("file4.txt","a") as f:
#     for i in ["avacado","dragon","mango","grapes","apple"]:
#         f.write(f"{i}\n")
# print("sucessfully append the data..")

#seek tell and truncate method in python
with open ("file.txt","r") as f:
    result=f.seek(5)
    print(f.tell()) #it tell us wat is pur position
    result=f.seek(10)
    print(result)
    print(f.tell())


with open ("file.txt",'w') as f:
    f.write("Hellow world")
    f.truncate(3)

#lamba function
x=lambda x,y:(x+y)/2

print(x(3,4))


#2 sum function with lambfa
sum=lambda x,y:x+y

print(sum(12,14))



