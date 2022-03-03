emp = int(input("Enter number of Employees: "))
name1 = []
age1 = []
desig1 = []
salary1 = []
for i in range(0,emp):
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    desig = input("Enter Designation: ")
    salary = int(input("Enter Salary: "))
    name1.append(name)
    age1.append(age)
    desig1.append(desig)
    salary1.append(salary)
print(name1)
print(age1)
print(desig1)
print(salary1)
