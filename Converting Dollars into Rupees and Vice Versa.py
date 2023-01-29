# Converting Dollars into Rupees and Vice Versa
A=float(input("Choose if you want convert rupees into dollar or vice versa (1 for rupees to dollar and 2 for dollar to ruppes)"))
if(A==1):
    R=float(input("Enter Amount in Rupees"))
    D=(R/70)
    print("Amount in Dollars is",D)
if(A==2):
    D=float(input("Enter Amount in Dollars"))
    R=(D*70)
    print("Amount in Rupees is",R)
