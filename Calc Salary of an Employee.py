# Calc Salary of an Employee
BS=int(input("Enter Basic Salary of an Employee"))
D=int(input("Enter DA of an Employee"))
H=int(input("Enter HRA of an Employee"))
TS=BS+D+H
print("Gross salary tax is",5)
G=TS*5/100
NS=TS-G
print("Net Salary is",NS)
