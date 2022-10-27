employees = {
1: {'firstName': 'Joe', 'lastName': 'Black', 'employeeId': 123},
2: {'firstName': 'Veronica', 'lastName': 'White', 'employeeId': 234},
3: {'firstName': 'Ali', 'lastName': 'East', 'employeeId': 421}
}
# adding an empty new dictionary as a value for a new key (i.e. a new item) in the parent dictionary
employees[4] = {}
# adding elements one at a time to the new child dictionary
employees[4]['firstName'] = 'Anna'
employees[4]['lastName'] = 'Zeu'
employees[4]['employeeId'] = 452
employees[4]['fullTime'] = True # It's ok to add additional elements to a child dict
employees[5] = {'firstName': 'Cara', 'lastName': 'Ozz', 'employeeId ': 333}



print(employees[3] ["employeeId"])

employees = {
    123: {"First Name: ": "Joe", "Last Name: ": "Black"},
    234: {"First Name: ": "Veronica", "Last Name: ": "White"},
    421: {"First Name: ": "Ali", "Last Name: ": "East"}
}

print(employees)

print(employees[123]["Last Name: "])


employees[234]["Last Name: "] = "Brown"
print(employees)

for employeeId, employeeInfo in employees.items():
    print("\nEmployee ID: {}".format(employeeId))
for key in employeeInfo:
    print("{0}: {1}".format(key,
employeeInfo[key]))
for key in employeeInfo:
    print("{0}: {1}".format(key,
employeeInfo[key]))