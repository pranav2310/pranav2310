# Calc Roots of Eqn
a=int(input("Enter coefficient of x^2"))
b=int(input("Enter coefficient of x"))
c=int(input("Enter constant"))
D=b**2-4*a*c
x1=(-b+D**1/2)/2*a
x2=(-b-D**1/2)/2*a
print("Roots of the equations are",x1 ,"and",x2)
