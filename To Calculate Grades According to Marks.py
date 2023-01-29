#To Calculate Grades According to Marks
M=int(input("Enter Your Marks"))
if(M<40):
    print("Your Grade is E")
if(M>=40 and M<=54):
    print("Your Grade is D")
elif(M>=55 and M<=69):
    print("Your Grade is C")
elif(M>=70 and M<=85):
    print("Your Grade is B")
elif(M>85):
    print("Your Grade is A")
