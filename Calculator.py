#Calculator
C=float(input("Enter 1 to ADD, 2 to SUBTRACT, 3 to DIVIDE and 4 to MULTIPLY two numbers"))
if(C==1):
    n1=float(input("Enter a number-"))
    n2=float(input("Enter a number-"))
    A=n1+n2
    print("Sum is",A)
if(C==2):
    n1=float(input("Enter a number-"))
    n2=float(input("Enter a number-"))
    S=n1-n2
    print("Difference is",S)
if(C==3):
    n1=float(input("Enter a number-"))
    n2=float(input("Enter a number-"))
    D=n1/n2
    print("Quotient is",D)
if(C==4):
    n1=float(input("Enter a number-"))
    n2=float(input("Enter a number-"))
    P=n1*n2
    print("Product is",P)
