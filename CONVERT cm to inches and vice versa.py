#CONVERT cm to inches and vice versa
A=float(input("Enter 1 to convert cm to inches and 2 to convert inches to cm"))
if(A==1):
    C=float(input("Enter length in cm"))
    I=C/2.54
    print("length in Inches is",I)
if(A==2):
    I=float(input("Enter length in inches"))
    C=I/2.54
    print("length in cm is",C)
