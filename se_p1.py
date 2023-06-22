import pandas as pd
import numpy as np
import openpyxl as op
from datetime import datetime
from tkinter import *

while(1):
    df1=pd.read_excel(r"C:\Users\Asit Singh\OneDrive\Documents\Record.xlsx")
    df2=pd.read_excel(r"C:\Users\Asit Singh\OneDrive\Documents\Active.xlsx")

    key=df2.columns
    d1={}
    for i in key:
        if(i=="Issue Time"):
            d1[i]=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        elif(i=="Equipment name"):
            continue
        else:
            print("Enter "+i+": ")
            d1[i]=input()

    rn=d1["Register Number"]
    
    arr=df1[df1["Register Number"]==rn].index.values
    if(arr.size!=0):
        ri=arr[-1]

    B=False
    if df2.isin([rn]).any().any():
        print("Equipment returned?: ")
        root=Tk()
        root.attributes('-topmost',True)
        root.title("Confirm status!")
    
        def click_yes():
            global A
            A=True
            root.destroy()
            return A
    
        def click_no():
            global A
            A=False
            root.destroy()
            return A
    
        blank1=Label(root, text="\t")
        blank2=Label(root, text="\t")
        myText=Label(root, text="Equipment returned?")
        myButton1=Button(root, text="Yes",padx=30,command=click_yes)
        myButton2=Button(root, text="No",padx=30,command=click_no)
        
        blank1.grid(row=0, column=0)
        blank2.grid(row=0, column=4)
        myText.grid(row=0,column=2)
        myButton1.grid(row=1, column=1)
        myButton2.grid(row=1, column=3)
        
        root.mainloop()
        if(A):
            df2.drop(df2[df2["Register Number"]==rn].index,axis=0,inplace=True)
            df1.loc[ri,"Return Time"]=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        else:
            er=Tk()
            er.geometry("400x60")
            myLabel=Label(er,text="Return equipment first.",fg="Red", font=("Arial",25))
            myLabel.pack()
            er.mainloop()
    else:
        ddm = Tk()
        ddm.title("Issue Equipment")
        ddm.geometry("320x120")
        ddm.attributes('-topmost',True)
    
        clicked = StringVar()
    
        def click_cancel():
            global B
            B=True
            ddm.destroy()
            
        def click_submit():
            d1["Equipment name"]=clicked.get()
            ddm.destroy()
        
        options=[
            "Football",
            "Volleyball",
            "Basketball",
            "Cricket ball and bat",
            "Badminton (Singles)",
            "Badminton (Doubles)"
            ]
    
        myLabel1=Label(ddm, text="Name: ", font=("Arial",12,"bold"))
        myLabel2=Label(ddm, text=d1["Name"], font=("Arial",12))
        myLabel3=Label(ddm, text="Register Number: ", font=("Arial",12,"bold"))
        myLabel4=Label(ddm, text=d1["Register Number"], font=("Arial",12))
        myLabel5=Label(ddm, text="Equipment: ", font=("Arial",12,"bold"))
        drop=OptionMenu(ddm, clicked, *options)
        myButton1=Button(ddm, text="Submit",padx=28, command=click_submit)
        myButton2=Button(ddm, text="Cancel",padx=28, command=click_cancel)

        menu_width=len(options[4])
        drop.config(width=menu_width)
        
        myLabel1.grid(row=0 ,column=0)
        myLabel2.grid(row=0 ,column=1)
        myLabel3.grid(row=1 ,column=0)
        myLabel4.grid(row=1 ,column=1)
        myLabel5.grid(row=2 ,column=0)
        drop.grid(row=2, column=1) 
        myButton1.grid(row=3 ,column=0)
        myButton2.grid(row=3 ,column=1)
    
        ddm.mainloop()
        
        if(B):
            continue
        else:
            d=pd.DataFrame(d1,index=[0])
            df2=pd.concat([df2,d],ignore_index=True)
            df1=pd.concat([df1,d],ignore_index=True)
    
    df1.to_excel(r"C:\Users\Asit Singh\OneDrive\Documents\Record.xlsx",index=False)
    df2.to_excel(r"C:\Users\Asit Singh\OneDrive\Documents\Active.xlsx",index=False)
