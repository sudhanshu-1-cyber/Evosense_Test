from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import numpy as np

class Contact:
    def __init__(self, root):       #root -  window name     
        self.root=root          #initialize self
        
        img = Image.open(r"EvoSense_login\\assets\\img\\bg.jpg")
        img_width, img_height = img.size
        self.root.geometry(f"{img_width}x{img_height}+0+0") # set the window size to the image size
        self.root.title("Facial Recognition System")

        title_lbl=Label(self.root, text="Contact Information", font=("Times New Roman", 35, "bold"), bg="black", fg="#74a7d2")
        title_lbl.place(x=0, y=0, width=img_width, height=60)

        img = img.resize((img_width, img_height), Image.ADAPTIVE) 
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=60, relheight=1, relwidth=1)

        frame = Frame(self.root, bg="black")
        frame.place(x=430, y=240, width=450, height=200)

        phn_no = Label(frame, text="Phone No. -", font=("times new roman", 18, "bold"), fg="#74a7d2", bg="black")
        phn_no.place(x=95, y=50)

        phn_no = Label(frame, text="869740xxxx", font=("times new roman", 17, "bold"), fg="white", bg="black")
        phn_no.place(x=225, y=50)

        email = Label(frame, text="Email -", font=("times new roman", 18, "bold"), fg="#74a7d2", bg="black")
        email.place(x=95, y=110)

        email = Label(frame, text="abc@gmail.com", font=("times new roman", 17, "bold"), fg="white", bg="black")
        email.place(x=180, y=110)

if __name__ == "__main__":
    root = Tk()
    obj = Contact(root)
    root.mainloop()