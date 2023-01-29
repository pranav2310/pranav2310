# Convert km to miles and vice versa
A=float(input("Choose if you want to convert kilometer to miles or vice versa (Enter 1 to convert km to miles and 2 to convert miles to km)"))
if(A==1):
    K=float(input("Enter the distance in km"))
    M=K/0.621
    print("Distance in miles is",M)
if(A==2):
    M=float(input("Enter the distance in miles"))
    K=M*0.621
    print("Distance in km is",K)
