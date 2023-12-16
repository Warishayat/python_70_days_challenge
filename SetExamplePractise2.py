# You are given a list of sets, where each set represents a
# group of students enrolled in a course. Write a Python function to find the
# intersection of all these sets, i.e., the set of students who are enrolled
# in all the courses.
course1_students = {"waris","Alice", "Bob", "Charlie", "David", "Eva"}
course2_students = {"waris", "Eva", "Grace", "Hank", "Ivy"}
course3_students = {"waris", "David", "Hank", "Ivy", "Jack"}
course4_students = {"waris", "Bob", "Charlie", "David", "Eva", "Hank"}


students_list = [course1_students, course2_students, course3_students, course4_students]

intersection_result=set.intersection(*students_list)

print("The student who enrolled in  all clases:",intersection_result)