# Calculating Compound Intrests
P=int(input("Enter Principle"))
R=int(input("Enter Rate of Intrest"))
T=int(input("Enter Time in Years"))
CI=P*(1+R/100)**T
A=P+CI
print("Compound Intrest is",CI ,"Amount is",A)
