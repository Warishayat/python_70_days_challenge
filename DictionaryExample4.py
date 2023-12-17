# Use the keys(), values(), and items() methods on a dictionary
# and print the results.
# Create two dictionaries and merge them into a new dictionary.


dic={'sp21366':"Mubahir",'sp21367':"Ali_shah",'sp2138':"Waris hayat",'sp21369':"Bilal_Aziz"}
dic2={'sp21370':"Raza Malik",'sp21371':"Hassan_raza",'sp21372':"Hasnain_shareef",'sp21373':"" }

dic.update(dic2)
dic3={}
dic3.update(dic) #2 dictionaries like di and dic2 are merge in dic3:
print(dic3)
print()
#dictioneries_key
print(dic3.keys())
#dictioneries_value
print(dic3.values())
#dictioneries_items()(where items present both key and values:)
print(dic3.items())