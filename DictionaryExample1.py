# Accessing and Modifying Elements:
# Create a dictionary representing a person 
# with keys such as "name," "age," and "city." Print out the person's name.
# Update the person's age in the dictionary
# and print the updated dictionary.

person={
    'name': "waris",
    'age': 22,
    'city':"islamabad"
}

# print(person)
person.update({'age':23})  #by this update method we can update any value 
print(person)
print(person.values())