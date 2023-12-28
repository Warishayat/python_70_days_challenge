
filepath="file.txt"
with open(filepath,'r')as file:
    path=file.readlines()   #
    
print("It will read the all file in the form of list:",file)




#writelines() the out will be in a single line 
lines_to_write = ["Line 1: Hello, World!", "Line 2: Python is great.", "Line 3: File handling example."]
with open(filepath,"w") as file:
    path=file.writelines(lines_to_write)
    
print("Data added:")

#writlines() that print the output in the newlines (filehandling....) 
lines_to_write_with_newlines = ["Line 1: Hello, World!\n", "Line 2: Python is great.\n", "Line 3: File handling example.\n"]
with open(filepath,"w") as writelanes:
    printkarvao=writelanes.writelines(lines_to_write_with_newlines)
print("Succesfully added  new datawith new lines")


#now append the new thing in the existing file....
append_data=["Name","Age","Department","Salary",
"John","30","HR\n","50000",
"Alice","25","IT\n","60000",
"Bob","35","Finance\n","55000",
"Eva"",28","Marketing\n","48000",
"Charlie","32","IT\n","52000"]
      #the file path
with open(filepath,"a") as file:
    file.writelines(append_data)

print("Append data scuuesfully:-)")


