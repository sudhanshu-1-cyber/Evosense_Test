from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import numpy as np

class Contact:
    def __init__(self, root):       #root -  window name     
        self.root=root          #initialize self
        self.root.geometry("1530x790+0+0") #set geometary of the window
        self.root.title("Facial Recognition System")

        title_lbl=Label(self.root, text="Contact Infromation", font=("Times New Roman",35,"bold"),bg="black", fg="#74a7d2")
        title_lbl.place(x=0, y=0, width=1300, height=60)

        img=Image.open(r"C:\Face_recog_system - Copy\bg.jpg")
        img=img.resize((1300, 700), Image.ADAPTIVE) 
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=60.2, relheight=1,relwidth=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=430,y=240,width=450,height=200)

        phn_no=Label(frame,text="Phone No. -",font=("times new roman",18,"bold"),fg="#74a7d2",bg="black")
        phn_no.place(x=95,y=50)

        phn_no=Label(frame,text="869740xxxx",font=("times new roman",17,"bold"),fg="white",bg="black")
        phn_no.place(x=225,y=50)

        email=Label(frame,text="Email -",font=("times new roman",18,"bold"),fg="#74a7d2",bg="black")
        email.place(x=95,y=110)

        email=Label(frame,text="abc@gmail.com",font=("times new roman",17,"bold"),fg="white",bg="black")
        email.place(x=180,y=110)

    
if __name__ == "__main__":
    root=Tk()
    obj=Contact(root)
    root.mainloop()