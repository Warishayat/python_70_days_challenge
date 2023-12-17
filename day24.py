#dictionary 
#dictionary is used for mapping.
dic={
    "name":"Waris",
    "class":"Bs-software-engineer",
    "Rollno":21368,
    "Cgpa":"A+",
    'Semester': "4",
    'setion':'A-AFTERNOON'
}

for key in dic:
    print(f"tha value corresponding to the {key} is {dic[key]}")

# print(dic["name"])
print(dic.values())
for key in dic:
    print(f"The value crosspomding to {key } is={dic[key]}")



emp={
    1:69,
    2:90,
    3:77,
    4:88,
}
emp2={
    577:77,
    588:90
}

emp.update(emp2)
print(emp)
emp.pop(577)
print(emp)
emp.clear()
print(emp)


print()
print()
print()
#python nested ditionary(ditionary with in dictionary)

student={
    'php':{'duration':2 ,'fees':200000},
    'java':{'duration':2 ,'fees':200000},
    'python':{'duration':2 ,'fees':200000},
    'django':{'duration':2 ,'fees':200000}
}

for key,values in student.items():
    print(f"The value against {key} is {values}")