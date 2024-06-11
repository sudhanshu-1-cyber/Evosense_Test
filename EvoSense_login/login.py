from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector
from main import Facial_Recognition_System

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1530x790+0+0")

        self.bg=ImageTk.PhotoImage(file=r"C:\Face_recog_system - Copy\bg.jpg")
        
        
        lbl_bg=Label(self.root,image=self.bg)  
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        welcome=Label(self.root,text="Welcome to Evosense",font=("times new roman",30,"bold"),fg="#74a7d2",bg="black")
        welcome.place(x=0,y=0,width=1300,height=65)

        welcome2=Label(self.root,text="(A multi-modal Voice Assistant)",font=("times new roman",15,"bold"),fg="white",bg="black")
        welcome2.place(x=0,y=50,width=1300,height=30)    

        frame=Frame(self.root,bg="black")
        frame.place(x=480,y=140,width=340,height=450)

        img1=Image.open(r"C:\Face_recog_system - Copy\robot.png")
        img1=img1.resize((100,100),Image.Resampling.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=620,y=165,width=70,height=70)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="#74a7d2",bg="black")
        get_str.place(x=95,y=100)

        # label
        username_lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username_lbl.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password_lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password_lbl.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"),show='*')
        self.txtpass.place(x=40,y=250,width=270)

        # ----------- Icon Images -----------

        img2=Image.open(r"C:\Face_recog_system - Copy\user1.jpg")
        img2=img2.resize((25,25),Image.Resampling.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(frame,image=self.photoimage2,bg="black",borderwidth=0)
        lblimg2.place(x=40,y=150,width=25,height=25)

        img3=Image.open(r"C:\Face_recog_system - Copy\lock-icon-vector-illustration.jpg")
        img3=img3.resize((25,25),Image.Resampling.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg3=Label(frame,image=self.photoimage3,bg="black",borderwidth=0)
        lblimg3.place(x=40,y=220,width=25,height=25)

        # LoginButton
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="#152e43",activeforeground="white",activebackground='#152e43')
        loginbtn.place(x=110,y=300,width=120,height=35)

        # RegisterButton
        registerbtn=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=15,y=350,width=160)

        # ForgotpassButton
        forgotpassbtn=Button(frame,text="Forgot Password",command=self.forgot_password_window,font=("times new roman",10,"bold"),borderwidth=0,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgotpassbtn.place(x=10,y=370,width=160)


    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All fields are required")
        elif self.txtuser.get()=="abc" and self.txtpass.get()=="xyz":
            messagebox.showinfo("Success","Welcome to Face Recognition System")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="*E@$y007",database="face_recognizer")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",
            (
                self.txtuser.get(),
                self.txtpass.get()
            ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid username & password")
            else:
                open_main=messagebox.askyesno("Access","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Facial_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
                    
            conn.commit()
            conn.close()


    # --------------- Reset Password ------------------
    def reset_password(self):
        if self.combo_security_Q.get()=="Select" or self.security_A_entry.get()=="" or self.new_password_entry.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root2)
        
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="*E@$y007",database="face_recognizer")
                my_cursor=conn.cursor()
                query=("select * from register where email=%s and securityQ=%s and securityA=%s")
                value=(self.txtuser.get(),self.combo_security_Q.get(),self.security_A_entry.get())
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please enter the correct answer",parent=self.root2)
                else:
                    query=("update register set password=%s where email=%s")
                    value=(self.new_password_entry.get(),self.txtuser.get())
                    my_cursor.execute(query,value)

                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Info","Your password has been reset, please login with new password",parent=self.root2)
                    self.root2.destroy()
                    self.txtuser.focus()
                    
            except Exception as es:
                messagebox.showerror("Error",f"Error due to:{str(es)}",parent=self.root2)


    # --------------- Forgot Password -------------------
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="*E@$y007",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","Please enter valid username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+480+170")

                l=Label(self.root2,text="Forgot Password",font=("times new roman",20,"bold"),fg="#74a7d2",bg="black")
                l.place(x=0,y=10,relwidth=1)
            
                security_Q=Label(self.root2,text="Select Security Question",font=("times new roman",15,"bold"),fg="black",bg="white")
                security_Q.place(x=50,y=80)

                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security_Q["values"]=("Select","Your Birth Place","Your Pet Name","Your Favourite Place")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)

                security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white")
                security_A.place(x=50,y=150)

                self.security_A_entry=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.security_A_entry.place(x=50,y=180,width=250)

                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white")
                new_password.place(x=50,y=220)

                self.new_password_entry=ttk.Entry(self.root2,font=("times new roman",15,"bold"),show='*')
                self.new_password_entry.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_password,font=("times new roman",15,"bold"),fg="white",bg="#152e43")
                btn.place(x=100,y=290,width=100)
                

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1530x790+0+0")

        # ---------- Variables ----------
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()

        # -------- Background image ----
        self.bg=ImageTk.PhotoImage(file=r"C:\Face_recog_system - Copy\bg.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        # ---------- Main Frame -------------
        frame=Frame(self.root,bg="white")
        frame.place(x=350,y=100,width=700,height=500)

        register_lbl=Label(frame,text="Register",font=("times new roman",20,"bold"),fg="#152e43",bg="white")
        register_lbl.place(x=20,y=20)

        # ---------- Label and entry ----------

        # ------ row 1
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.fname_entry.place(x=50,y=130,width=250)

        lname=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white")
        lname.place(x=370,y=100)

        self.lname_entry=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.lname_entry.place(x=370,y=130,width=250)

        # -------- row 2
        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white")
        contact.place(x=50,y=170)

        self.contact_entry=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        self.contact_entry.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white")
        email.place(x=370,y=170)

        self.email_entry=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.email_entry.place(x=370,y=200,width=250)

        # --------- row 3
        security_Q=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),fg="black",bg="white")
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your Pet Name","Your Favourite Place")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)

        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white")
        security_A.place(x=370,y=240)

        self.security_A_entry=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15,"bold"))
        self.security_A_entry.place(x=370,y=270,width=250)

        # --------- row 4
        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white")
        pswd.place(x=50,y=310)

        self.pswd_entry=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"),show='*')
        self.pswd_entry.place(x=50,y=340,width=250)

        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white")
        confirm_pswd.place(x=370,y=310)

        self.confirm_pswd_entry=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15,"bold"),show='*')
        self.confirm_pswd_entry.place(x=370,y=340,width=250)

        # ------------ checkbutton ------------
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I agree with the Terms & Conditions",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)

        # --------- buttons --------
        img=Image.open(r"C:\Face_recog_system - Copy\register.jpg")
        img=img.resize((200,70),Image.Resampling.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2")
        b1.place(x=50,y=420,width=200)

        img1=Image.open(r"C:\Face_recog_system - Copy\login.jpg")
        img1=img1.resize((200,70),Image.Resampling.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2")
        b1.place(x=370,y=420,width=200)


    # ------------- Function Declaration ----------
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password does not match")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree to our Terms & Condition")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="*E@$y007",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist, please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",
                (
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_securityQ.get(),
                    self.var_securityA.get(),
                    self.var_pass.get()

                ))

            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Registered successfully!!")

    def return_login(self):
        self.root.destroy()


if __name__ == "__main__":
    main()