import os
os.mkdir("Data")
for i in range(1,100):
    os.mkdir(f"data/tutorial{i+1}")
#how to create 100 folders/files.
folder=os.listdir("Data")
print(folder)


cmd="getcwd"
os.system(cmd)

#how to remove some file from the compueter:
import os
file="Python NoteBook"
location="C:\Users\Waris Hayyat\Desktop"
path = os.path.join(location, file)
os.remove(path)


#import time
import time
curr=time.time()
print("The current time is",curr)

#import date

from datetime import date
today= date.today()
print(today)
