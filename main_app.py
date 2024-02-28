from tkinter import *
from tkinter import messagebox
import os
import pandas as pd
import csv
from Face_detection import *
from Face_detection_train import *
from detect_mask_video import *
from face_reco import *
import pyttsx3
from voice_test import *

win = Tk() 
win.geometry("312x324")
def voice_message(text):

    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  
    engine.say(text)
    engine.runAndWait()


def registration():
    def register():
        name=entry_1.get()
        email=entry_02.get()
        gender=var.get()
        age=entry_03.get()
        print(name,email,gender,age)
        if name=="" or email=="" or age=="":
            messagebox.showinfo( "Alert", "Insertion failed Check entered data")
        else:
            if os.path.exists("data.csv"):
                df=pd.read_csv("data.csv")
                print(len(df))
                Id=len(df)+1
                with open("data.csv","a+",) as csvFile: 
                     writer = csv.writer(csvFile, delimiter=",")
                     writer.writerow([Id,name,email,gender,age])
                messagebox.showinfo( "Alert", "User Added")
                voice_message("Please face the camera")
                detection1(Id)
                messagebox.showinfo( "Alert", "Face Added to the database")
                
            else:
                print("File not found")

    #         base.destroy()
            
        
    base = Tk()  
    base.geometry('500x500')  
    base.title("Registration Form")  
      
    labl_0 = Label(base, text="Registration form",width=20,font=("bold", 20))  
    labl_0.place(x=90,y=53)  
      
      
    labl_1 = Label(base, text="FullName",width=20,font=("bold", 10))  
    labl_1.place(x=80,y=130)  
      
    entry_1 = Entry(base)  
    entry_1.place(x=240,y=130)  
      
    labl_2 = Label(base, text="Email",width=20,font=("bold", 10))  
    labl_2.place(x=68,y=180)  
      
    entry_02 = Entry(base)  
    entry_02.place(x=240,y=180)  
      
    labl_3 = Label(base, text="Gender",width=20,font=("bold", 10))  
    labl_3.place(x=70,y=230)  
    var = IntVar()  
    r1=Radiobutton(base, text="Male",padx = 5, variable=var, value=1)
    r1.place(x=235,y=230)  
    r2=Radiobutton(base, text="Female",padx = 20, variable=var, value=2)
    r2.place(x=310,y=230)  
      
    labl_4 = Label(base, text="Age:",width=20,font=("bold", 10))  
    labl_4.place(x=70,y=280)  
      
      
    entry_03 = Entry(base)  
    entry_03.place(x=240,y=280)  
      
    btn=Button(base, text='Submit',width=20,bg='brown',fg='white',command = register)
    btn.place(x=180,y=380)  
    base.mainloop()  
    print("Registration form is created successfully...")
def detection_call():
    voice_message("Detecting the presence of mask.")
    mask_detection()
    voice_message("Please Remove the Mask for Face Recognition")
    Id=detection()
    df=pd.read_csv("data.csv")
    user=df.loc[df['Id'] == Id]
    print(user)
    user=user["Name"]
    voice_message("Welcome"+ user+". Please use the command to execute")
    val=recognize()
    #detection_call()
        
#     messagebox.showinfo( "Info", "Training completed")
    
def homepage():
    top = Tk() 
    top.geometry("900x600")
    
    L1 = Label(top, text = "Admin Home",bd = 5,font=('Arial', 35))
    L1.place(x = 270,y = 30)
    b1 = Button(top, text = "User Registration",justify="center",width=20,height=10,command = registration)
    b1.place(x = 100,y = 250)
    b2 = Button(top, text = "Start Training",justify="center",width=20,height=10,command = TrainImage)
    b2.place(x = 350,y = 250)
    b3 = Button(top, text = "Start Recognition",justify="center",width=20,height=10,command = detection_call)
    b3.place(x = 600,y = 250)
    top.title("Homepage")
    top.mainloop()
    
# homepage()

def login():
    if E1.get()=="admin" and E2.get()=="admin":
        messagebox.showinfo( "Alert", "Login Successful")
        win.destroy()
        homepage()
    else:
        messagebox.showinfo( "Alert", "User Not Found")

L = Label(win, text = "Login",bd = 5,font=('Arial', 25))
L.place(x = 100,y = 30)

L1 = Label(win, text = "User Name:",bd = 5)
L1.place(x = 10,y = 100)

E1 = Entry(win, bd = 5)
E1.place(x = 100,y = 100)

L2 = Label(win, text = "Password:",bd = 5)
L2.place(x = 10,y = 200)

E2 = Entry(win,show ="*", bd = 5)
E2.place(x = 100,y = 200)

B = Button(win, text = "Login", command = login)
B.place(x = 120,y = 250)

win.title("User Identification System")
win.mainloop()