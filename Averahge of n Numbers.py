# Calculating Average of n numbers
n=int(input("Enter the Number of Values to calculate average"))
s=0
i=0
while i < n:
    i=i+1
    a=int(input("Enter a Number"))
    s=s+a
A=s/n
print("Average is", A)
