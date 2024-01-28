#today i will cover the seek(),tell() & truncat function....

# with open ("myfile.txt",'r') as f:
    
#     result=f.seek(10) #move the 10 byte forward.

#     print(f.tell())    #it tell us about where we are
#     result1=f.read(10)
#     print(result1)


with open ("Tetxt31.txt",'w') as f:
    f.write("Hellow world")
    f.truncate(3)