# This Project was made using Jupyter notebook and MySQL 5.7.
import mysql.connector
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="online_shopping")
mycursor=mydb.cursor()
n=input("To Go To Main Menu enter 'Yes',else 'No'")
while(n=='Yes')or (n=='yes'):
    m=int(input("Welcome To Main Menu\nEnter 0 To Display Data\nEnter 1 To Add a New Row\nEnter 2 To Update Data\nEnter 3 To Graphically Analyse Data\nEnter 4 To Delete a Row\nEnter 5 to export data in .csv format\nEnter 6 to Logout"))
    if(m==0):
        print("Type 'C' for Customer Information\nType 'S' for Stock information\nType 'D' for Delivery Info\nType 'B' FOR Bill Info ")
        T=input()
        if (T=='s')or (T=='S'):
            mycursor.execute("select * from stock")
            myrecords=mycursor.fetchall()
            print(pd.DataFrame(myrecords,columns=['Product Name','Product Id','Stock','Product Weight','Product Price']))
        elif T=='c'or T=='C':
            mycursor.execute("select * from customer_info")
            myrecords=mycursor.fetchall()
            print(pd.DataFrame(myrecords,columns=['Customer Name','Customer Phone No','Customer Id','Customer Address','Order Placed','Order Cancelled']))
        elif T=='d'or T=='D':
            mycursor.execute("select * from delivery")
            myrecords=mycursor.fetchall()
            print(pd.DataFrame(myrecords,columns=['Order Id','Delivery Time','Product Recieved','Product Returned','Customer Id','Product Id']))
        elif T=='b'or T=='B':
            mycursor.execute("select * from bill_info")
            myrecords=mycursor.fetchall()
            print(pd.DataFrame(myrecords,columns=['Bill Id','Amount Paid','Customer Id','Order Id']))
    elif m==1:
        print("Type 'C' to add a new Row to Customer Information Table\nType 'S' to add a new Row to Stock information Table\nType 'D' to add a new Row to Delivery Info Table\nType 'B' to add a new Row to Bill Info Table")
        t=input()
        if (t=='s') or (t=='S'):
            s="Rs."
            Pn=input("Enter Product Name")
            Pi=input("Enter Product Id")
            S=int(input("Enter Stock amount"))
            Pd=input("Enter Weight of the Product in g")
            Pr=int(input("Enter Price of The Product"))
            mycursor.execute("insert into stock values('"+Pn+"','"+Pi+"','"+str(S)+"','"+Pd+"','"+str(Pr)+"')")
            mydb.commit()
        elif (t=='c') or (t=='C'):
            Cn=input("Enter Customer Name")
            Cp=int(input("Enter Customer Phno"))
            Ci=input("Enter Customer Id")
            Add=input("Customer Address")
            OP=input("No. of Order Placed")
            OC=input("No. of Order Cancelled")
            mycursor.execute("insert into customer_info values('"+Cn+"','"+str(Cp)+"','"+Ci+"','"+Add+"','"+OP+"','"+OC+"')")
            mydb.commit()
        elif t=='d' or t=='D':
            oi=input("Enter Order Id")
            dt=int(input("Enter Delivery Time"))
            p=input("Enter y if product was recieved n if product was not recieved")
            pr=input("Enter y if returned else n")
            Ci=input("Enter Customer id")
            pi=input("Enter product id")
            mycursor.execute("insert into delivery values('"+oi+"','"+str(dt)+"','"+p+"','"+pr+"','"+Ci+"','"+pi+"')")
            mydb.commit()
        elif t=='b'or t=='B':
            bi=input("Enter Bill Id")
            a=int(input("Enter Amount Paid"))
            ci=input("Enter Customer Id")
            oi=input("Enter Order Id")
            mycursor.execute("insert into bill_info values('"+bi+"','"+str(a)+"','"+ci+"','"+oi+"')")
            mydb.commit()
    elif m==2:
        print("Type 'C' to update data in Customer Information Table\nType 'S' to update data in Stock information Table\nType 'D' to update data in Delivery Info Table\nType 'B' to update Data in Bill Info Table")
        t=input()
        if t=='s'or t=='S':
            mycursor.execute("select * from stock")
            myrecords=mycursor.fetchall()
            print(pd.DataFrame(myrecords,columns=['Product Name','Product Id','Stock','Product Weight','Product Price']))
            col=input("Enter column name")
            data=input("Enter the changed value")
            con=input("Enter the product id")
            mycursor.execute("update stock set "+col+"='"+data+"' where product_id='"+con+"';")
            mydb.commit()
            print("Data succesfully changed")
        if t=='c'or t=='C':
            mycursor.execute("select * from customer_info")
            myrecords=mycursor.fetchall()
            print(pd.DataFrame(myrecords,columns=['Customer Name','Customer Phone No','Customer Id','Customer Address','Order Placed','Order Cancelled']))
            col=input("Enter column name")
            data=input("Enter the changed value")
            con=input("Enter the customer id")
            mycursor.execute("update customer_info set "+col+"='"+data+"' where customer_id='"+con+"';")
            mydb.commit()
            print("Data succesfully changed")
        if t=='d' or t=='D':
            mycursor.execute("select * from delivery")
            myrecords=mycursor.fetchall()
            print(pd.DataFrame(myrecords,columns=['Order Id','Delivery Time','Product Recieved','Product Returned','Customer Id','Product Id']))
            col=input("Enter column name")
            data=input("Enter the changed value")
            con=input("Enter the order id")
            mycursor.execute("update delivery set "+col+"='"+data+"' where order_id='"+con+"';")
            mydb.commit()
            print("Data succesfully changed")
        if t=='b'or t=='B':
            mycursor.execute("select * from bill_info")
            myrecords=mycursor.fetchall()
            print(pd.DataFrame(myrecords,columns=['Bill Id','Amount Paid','Customer Id','Order Id']))
            data=input("Enter the changed Amount Paid")
            con=input("Enter the bill id")
            mycursor.execute("update bill_info set amount_paid='"+data+"' where bill_id='"+con+"';")
            mydb.commit()
            print("Data succesfully changed")
    elif m==3:
        print("Type 'C' to See which Customer has Placed Most number of orders\nType 'S' for Stock Chart\nType 'B' for Amount Paid Chart ")
        T=input()
        if (T=='s')or (T=='S'):
            mycursor.execute("select * from stock;")
            myrecords=mycursor.fetchall()
            x=[]
            y=[]
            for i in myrecords:
                x.append(i[0])
                y.append(i[2])
            i=np.arange(len(x))
            plt.xticks(i,x,rotation=30)
            plt.title("Stock Chart")
            plt.xlabel("Name of Product")
            plt.ylabel("Stock")
            plt.bar(x,y)
            plt.show()
        elif (T=='c')or (T=='C'):
            mycursor.execute("select * from customer_info;")
            myrecords=mycursor.fetchall()
            x=[]
            y=[]
            for i in myrecords:
                x.append(i[0])
                y.append(i[4])
            i=np.arange(len(x))
            plt.xticks(i,x,rotation=30)
            plt.title("Customer Who Order's The Most")
            plt.ylabel("Order Placed")
            plt.xlabel("Customer Name")
            plt.bar(x,y)
            plt.show()
        elif (T=='b')or (T=='B'):
            mycursor.execute("select * from bill_info;")
            myrecords=mycursor.fetchall()
            x=[]
            y=[]
            for i in myrecords:
                x.append(i[0])
                y.append(i[1])
            i=np.arange(len(x))
            plt.xticks(i,x,rotation=30)
            plt.title("Amount Paid Chart")
            plt.xlabel("Bill Id")
            plt.ylabel("Amount")
            plt.bar(x,y)
            plt.show()
    elif m==4:
        print("Type 'C' for Customer Information\nType 'S' for Stock information\nType 'D' for Delivery Info\nType 'B' FOR Bill Info ")
        T=input()
        if (T=='s')or (T=='S'):
            con=input("Enter Product Id")
            mycursor.execute("Delete From Stock where Product_Id='"+con+"'")
        if (T=='c')or (T=='C'):
            con=input("Enter Customer Id")
            mycursor.execute("Delete From Customer_Id where Customer_Id='"+con+"'")
        if (T=='d')or (T=='D'):
            con=input("Enter Order Id")
            mycursor.execute("Delete From Delivery where Order_Id='"+con+"'")
        if (T=='b')or (T=='B'):
            con=input("Enter Bill Id")
            mycursor.execute("Delete From Bill_Info where Bill_Id='"+con+"'")
    elif m==5:
        print("Type 'C' for Customer Information\nType 'S' for Stock information\nType 'D' for Delivery Info\nType 'B' FOR Bill Info ")
        T=input()
        if (T=='s')or (T=='S'):
            mycursor.execute("select * from stock")
            myrecords=mycursor.fetchall()
            df=pd.DataFrame(myrecords,columns=['Product Name','Product Id','Stock','Product Weight','Product Price'])
            df.to_csv(r"D:\CSV\Stock.csv")
        elif T=='c'or T=='C':
            mycursor.execute("select * from customer_info")
            myrecords=mycursor.fetchall()
            df=pd.DataFrame(myrecords,columns=['Customer Name','Customer Phone No','Customer Id','Customer Address','Order Placed','Order Cancelled'])
            df.to_csv(r"D:\CSV\Customer Info.csv")
        elif T=='d'or T=='D':
            mycursor.execute("select * from delivery")
            myrecords=mycursor.fetchall()
            df=pd.DataFrame(myrecords,columns=['Order Id','Delivery Time','Product Recieved','Product Returned','Customer Id','Product Id'])
            df.to_csv(r"D:\CSV\Delivery.csv")
        elif T=='b'or T=='B':
            mycursor.execute("select * from bill_info")
            myrecords=mycursor.fetchall()
            df=pd.DataFrame(myrecords,columns=['Bill Id','Order Id','Customer Id','Amount Paid'])
            df.to_csv(r"D:\CSV\Bill Info.csv")
    elif m==6:
        print("You have succesfully Logged Out")
        break
else:
    print("You have succesfully Logged Out")
