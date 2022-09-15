# Health Management System
# 3clients -  harry , rohan and hamad
# total 6 files
# write a function that when executed takes as input client name
# example- [<time>] diet/exercise

def getdate():
    import datetime
    return datetime.datetime.now()
dt=str(getdate())
t="yes"
while t=="yes":
    hm=int(input("Enter 1 to add data about Harry, 2 to add data about Rohan, 3 to add data about Hammad"))
    if hm==1:
        hm1=input("Enter diet to add data about Diet or Enter exercise to add data about Exercise")
        if hm1=="diet":
            d=input("Enter Diet taken by harry Today")
            f=open("harrydiet.txt", "a")
            f.write(dt)
            f.write("\t")
            f.write(d)
            f.write("\n")
            f.close()
            t=input("Enter yes if u want to continue adding data")
        elif hm1=="exercise":
            d = input("Enter the exercise done by harry Today")
            f = open("harryexercise.txt", "a")
            f.write(dt)
            f.write("\t")
            f.write(d)
            f.write("\n")
            f.close()
            t = input("Enter yes if u want to continue adding data")
            f.close()
    elif hm==2:
        hm1 = input("Enter diet to add data about Diet or Enter exercise to add data about Exercise")
        if hm1 == "diet":
            d = input("Enter Diet taken by rohan Today")
            f = open("rohandiet.txt", "a")
            f.write(dt)
            f.write("\t")
            f.write(d)
            f.write("\n")
            f.close()
            t = input("Enter yes if u want to continue adding data")
            f.close()

        elif hm1 == "exercise":
            d = input("Enter the exercise done by rohan Today")
            f = open("rohanexercise.txt", "a")
            f.write(dt)
            f.write("\t")
            f.write(d)
            f.write("\n")
            f.close()
            t = input("Enter yes if u want to continue adding data")
            f.close()
    elif hm==3:
        hm1 = input("Enter diet to add data about Diet or Enter exercise to add data about Exercise")
        if hm1 == "diet":
            d = input("Enter Diet taken by hammad Today")
            f = open("hammaddiet.txt", "a")
            f.write(dt)
            f.write("\t")
            f.write(d)
            f.write("\n")
            f.close()
            f.close()
            t = input("Enter yes if u want to continue adding data")
        elif hm1 == "exercise":
            d = input("Enter the exercise done by hammad Today")
            f = open("hammadexercise.txt", "a")
            f.write(dt)
            f.write("\t")
            f.write(d)
            f.write("\n")
            f.close()
            f.close()
            t = input("Enter yes if u want to continue adding data")
    else:
        print("Error Data doesn't exist")
        t=input("If You want to add data about harry, rohan or hammad enter yes else enter no")
print("Thank You for Helping us monitoring ur Lifestyle for Better Health")
