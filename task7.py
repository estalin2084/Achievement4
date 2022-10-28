#A program to allow users to register in a course


print("\t","\t","\t","Welcome to EP Learning Institution!")
print("")
print("Please introduce your information in the fields below and select your courses.")
print("")

firstName = input("Please enter your first name: ")
lastName = input("Please enter yoru last name: ")
studentNumber = input("Please enter your student number: ")
student_info = [firstName, lastName, studentNumber]
separator = " "
dash = " - "
print("")
print("Please choose which course you'd like to register in: ")
courseCodes = {1 :'ENG123', 2 :'HIS456', 3: 'PROG789', 4: 'MATH639'}
courseName = {"ENG123": "English Class", "HIS456": "History of the Americas", "PROG789": "Programming III", "MATH639": "Mathematics"}

for i, v in courseCodes.items():
    print(str(i) + " - " + v)

print(" ")

courseSelection= input("Select your courses: ")
selectedCourses=[]
print("")
iterate_list = courseSelection.split(",")
for x in iterate_list:
    selectedCourses.append(courseCodes.get(int(x)))

print("Student information:", separator.join(student_info))
print ("Courses selected:") 
for v in selectedCourses:
    print(v + " - " + courseName.get(v))

