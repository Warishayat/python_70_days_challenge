# You are given a list of names. Write a Python function that takes this list of names and 
# returns a new list containing the lengths of the names that are longer than 5 characters.
#  Use the walrus operator in your solution.

def long_names_length(name_list):
    list=[]
    for name in name_list:
        if (length:=(len(name)))>=5:
            list.append(name)
    return list



names_list = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace"]
result = long_names_length(names_list)
print(result)