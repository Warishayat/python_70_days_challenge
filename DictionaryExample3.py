# Looping Through Dictionaries:
# Create a dictionary of at least 5 key-value pairs.
# Use a for loop to iterate over the dictionary and print each key 
# and its corresponding value.

dic={
    'name': "waris Hayat Abbasi","age":22, "Status":"student","Cnic":3740458865757,"Degree":"Software-Engineering",'rollnum':"Sp21368"

}


#we use foor loop to iterate the key to get the value:
for i in dic:
    print(f"{i}is = {dic[i]}")