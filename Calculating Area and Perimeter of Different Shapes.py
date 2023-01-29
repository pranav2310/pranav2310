K=input("Enter C for circle,  enter S for Square, Enter R for Rectangle, Enter T for Triangle")
if K=='C':
    #Calculating Area and Perimeter of a Circle
    r=int(input("Enter Radius of a Circle"))
    A=22/7*r**2
    C=22/7*2*r
    print("Area of the circle is ",A ,"Circumference of the Circle",C)
elif K=='S':
    #Calculating Area and Perimeter of a Square
    s=int(input("Enter length of the side of a square"))
    A=s**2
    P=4*s
    print("Area of the square is ",A ,"Perimeter of the square",P)
elif K=='R':
    #Calculating Area and Perimeter of a Rectangle
    l=int(input("Enter length of the rectangle"))
    b=int(input("Enter breadth of the rectangle"))
    A=2*(l+b)
    P=l*b
    print("Area of the rectangle is ",A ,"Perimeter of the rectangle is",P)
elif K=='T':
    #Calculateing Area and Perimeter of a Triangle
    a=int(input("Enter length of First Side"))
    b=int(input("Enter length of Second Side"))
    c=int(input("Enter length of Third Side"))
    P=a+b+c
    semi=P/2
    a=(semi*(semi-a)*(semi-b)*(semi-c))
    A=a**(1/2)
    print("Area of the Triangle is ",A ,"Perimeter of the Triangle is",P )
else: 
    print("Invalid Input")
