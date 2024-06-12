from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector
from main import Facial_Recognition_System


def main():
    win = Tk()
    app = Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1530x790+0+0")
        self.root.configure(bg="black")

        # Load background image
        self.bg = Image.open(r"EvoSense_login\\assets\\img\\bg.jpg")
        self.bg = ImageTk.PhotoImage(self.bg)

        # Create canvas to hold the background image
        self.canvas = Canvas(self.root, width=self.bg.width(), height=self.bg.height())
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg, anchor="nw")

        welcome = Label(self.root, text="Welcome to Evosense", font=("times new roman", 30, "bold"), fg="#74a7d2", bg="black")
        welcome.place(relx=0.5, rely=0.05, anchor=CENTER)

        welcome2 = Label(self.root, text="(A multi-modal Voice Assistant)", font=("times new roman", 15, "bold"), fg="white", bg="black")
        welcome2.place(relx=0.5, rely=0.1, anchor=CENTER)

        frame = Frame(self.root, bg="black")
        frame.place(relx=0.5, rely=0.55, anchor=CENTER, width=340, height=450)

        img1 = Image.open(r"EvoSense_login\\assets\\img\\robot.png")
        img1 = img1.resize((100, 100), Image.Resampling.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1, bg="black", borderwidth=0)
        lblimg1.place(relx=0.5, rely=0.27, anchor=CENTER, width=70, height=70)

        get_str = Label(frame, text="Get Started", font=("times new roman", 20, "bold"), fg="#74a7d2", bg="black")
        get_str.place(relx=0.5, rely=0.25, anchor=CENTER)

        username_lbl = Label(frame, text="Username", font=("times new roman", 15, "bold"), fg="white", bg="black")
        username_lbl.place(x=70, y=155)

        self.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=180, width=270)

        password_lbl = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        password_lbl.place(x=70, y=225)

        self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"), show='*')
        self.txtpass.place(x=40, y=250, width=270)

        img2 = Image.open(r"EvoSense_login\\assets\\img\\user1.jpg")
        img2 = img2.resize((25, 25), Image.Resampling.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(frame, image=self.photoimage2, bg="black", borderwidth=0)
        lblimg2.place(x=40, y=150, width=25, height=25)

        img3 = Image.open(r"EvoSense_login\\assets\\img\\lock-icon-vector-illustration.jpg")
        img3 = img3.resize((25, 25), Image.Resampling.LANCZOS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg3 = Label(frame, image=self.photoimage3, bg="black", borderwidth=0)
        lblimg3.place(x=40, y=220, width=25, height=25)

        loginbtn = Button(frame, command=self.login, text="Login", font=("times new roman", 15, "bold"), bd=3, relief=RIDGE, fg="white", bg="#152e43", activeforeground="white", activebackground='#152e43')
        loginbtn.place(x=110, y=300, width=120, height=35)

        registerbtn = Button(frame, text="New User Register", command=self.register_window, font=("times new roman", 10, "bold"), borderwidth=0, relief=RIDGE, fg="white", bg="black", activeforeground="white", activebackground="black")
        registerbtn.place(x=15, y=350, width=160)

        forgotpassbtn = Button(frame, text="Forgot Password", command=self.forgot_password_window, font=("times new roman", 10, "bold"), borderwidth=0, relief=RIDGE, fg="white", bg="black", activeforeground="white", activebackground="black")
        forgotpassbtn.place(x=10, y=370, width=160)

    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif self.txtuser.get() == "abc" and self.txtpass.get() == "xyz":
            messagebox.showinfo("Success", "Welcome to Face Recognition System")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="_Sudhanshu9.", database="face_recognizer")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",
                              (
                                  self.txtuser.get(),
                                  self.txtpass.get()
                              ))
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Invalid username & password")
            else:
                open_main = messagebox.askyesno("Access", "Access only admin")
                if open_main > 0:
                    self.new_window = Toplevel(self.root)
                    self.app = Facial_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return

            conn.commit()
            conn.close()

    def reset_password(self):
        if self.combo_security_Q.get() == "Select" or self.security_A_entry.get() == "" or self.new_password_entry.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root2)

        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="_Sudhanshu9.", database="face_recognizer")
                my_cursor = conn.cursor()
                query = ("select * from register where email=%s and securityQ=%s and securityA=%s")
                value = (self.txtuser.get(), self.combo_security_Q.get(), self.security_A_entry.get())
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Please enter the correct answer", parent=self.root2)
                else:
                    query = ("update register set password=%s where email=%s")
                    value = (self.new_password_entry.get(), self.txtuser.get())
                    my_cursor.execute(query, value)

                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Info", "Your password has been reset, please login with new password", parent=self.root2)
                    self.root2.destroy()
                    self.txtuser.focus()

            except Exception as es:
                messagebox.showerror("Error", f"Error due to:{str(es)}", parent=self.root2)

    def forgot_password_window(self):
        if self.txtuser.get() == "":
            messagebox.showerror("Error", "Please enter the email address to reset password")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="_Sudhanshu9.", database="face_recognizer")
            my_cursor = conn.cursor()
            query = ("select * from register where email=%s")
            value = (self.txtuser.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            if row == None:
                messagebox.showerror("Error", "Please enter valid username")
            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+480+170")

                l = Label(self.root2, text="Forgot Password", font=("times new roman", 20, "bold"), fg="#74a7d2", bg="black")
                l.place(relx=0.5, rely=0.1, anchor=CENTER)

                security_Q = Label(self.root2, text="Select Security Question", font=("times new roman", 15, "bold"), fg="black", bg="white")
                security_Q.place(relx=0.5, rely=0.2, anchor=CENTER)

                self.combo_security_Q = ttk.Combobox(self.root2, font=("times new roman", 15, "bold"), state="readonly")
                self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your Best Friend Name", "Your Pet Name")
                self.combo_security_Q.place(relx=0.5, rely=0.3, anchor=CENTER, width=200)
                self.combo_security_Q.current(0)

                security_A = Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"), fg="black", bg="white")
                security_A.place(relx=0.5, rely=0.4, anchor=CENTER)

                self.security_A_entry = ttk.Entry(self.root2, font=("times new roman", 15, "bold"))
                self.security_A_entry.place(relx=0.5, rely=0.5, anchor=CENTER, width=200)

                new_password = Label(self.root2, text="New Password", font=("times new roman", 15, "bold"), fg="black", bg="white")
                new_password.place(relx=0.5, rely=0.6, anchor=CENTER)

                self.new_password_entry = ttk.Entry(self.root2, font=("times new roman", 15, "bold"))
                self.new_password_entry.place(relx=0.5, rely=0.7, anchor=CENTER, width=200)

                btn = Button(self.root2, text="Reset", command=self.reset_password, font=("times new roman", 15, "bold"), fg="white", bg="green")
                btn.place(relx=0.5, rely=0.85, anchor=CENTER, width=150)

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1530x790+0+0")

        # Load background image
        self.bg = Image.open(r"EvoSense_login\\assets\\img\\bg2.jpg")
        self.bg = ImageTk.PhotoImage(self.bg)

        # Create canvas to hold the background image
        self.canvas = Canvas(self.root, width=self.bg.width(), height=self.bg.height())
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg, anchor="nw")

        # Main Frame
        frame = Frame(self.root, bg="black")
        frame.place(relx=0.5, rely=0.5, anchor=CENTER, width=800, height=550)

        register_lbl = Label(frame, text="REGISTER HERE", font=("times new roman", 20, "bold"), fg="#74a7d2", bg="black")
        register_lbl.place(relx=0.5, rely=0.1, anchor=CENTER)

        # Labels and Entry
        fname = Label(frame, text="First Name", font=("times new roman", 15, "bold"), bg="black", fg="white")
        fname.place(relx=0.2, rely=0.2, anchor=CENTER)

        self.fname_entry = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.fname_entry.place(relx=0.4, rely=0.2, anchor=CENTER, width=200)

        lname = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="black", fg="white")
        lname.place(relx=0.2, rely=0.3, anchor=CENTER)

        self.lname_entry = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.lname_entry.place(relx=0.4, rely=0.3, anchor=CENTER, width=200)

        contact = Label(frame, text="Contact No", font=("times new roman", 15, "bold"), bg="black", fg="white")
        contact.place(relx=0.2, rely=0.4, anchor=CENTER)

        self.contact_entry = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.contact_entry.place(relx=0.4, rely=0.4, anchor=CENTER, width=200)

        email = Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="black", fg="white")
        email.place(relx=0.2, rely=0.5, anchor=CENTER)

        self.email_entry = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.email_entry.place(relx=0.4, rely=0.5, anchor=CENTER, width=200)

        security_Q = Label(frame, text="Select Security Question", font=("times new roman", 15, "bold"), bg="black", fg="white")
        security_Q.place(relx=0.2, rely=0.6, anchor=CENTER)

        self.combo_security_Q = ttk.Combobox(frame, font=("times new roman", 15, "bold"), state="readonly")
        self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your Best Friend Name", "Your Pet Name")
        self.combo_security_Q.place(relx=0.4, rely=0.6, anchor=CENTER, width=200)
        self.combo_security_Q.current(0)

        security_A = Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="black", fg="white")
        security_A.place(relx=0.2, rely=0.7, anchor=CENTER)

        self.security_A_entry = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.security_A_entry.place(relx=0.4, rely=0.7, anchor=CENTER, width=200)

        password = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="black", fg="white")
        password.place(relx=0.2, rely=0.8, anchor=CENTER)

        self.password_entry = ttk.Entry(frame, font=("times new roman", 15, "bold"), show='*')
        self.password_entry.place(relx=0.4, rely=0.8, anchor=CENTER, width=200)

        conf_password = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="black", fg="white")
        conf_password.place(relx=0.2, rely=0.9, anchor=CENTER)

        self.conf_password_entry = ttk.Entry(frame, font=("times new roman", 15, "bold"), show='*')
        self.conf_password_entry.place(relx=0.4, rely=0.9, anchor=CENTER, width=200)

        # Register Button
        registerbtn = Button(frame, text="Register", command=self.register_data, font=("times new roman", 15, "bold"), bd=3, relief=RIDGE, fg="white", bg="#152e43", activeforeground="white", activebackground="#152e43")
        registerbtn.place(relx=0.5, rely=1.0, anchor=CENTER, width=120)

    def register_data(self):
        if self.fname_entry.get() == "" or self.email_entry.get() == "" or self.combo_security_Q.get() == "Select":
            messagebox.showerror("Error", "All fields are required")
        elif self.password_entry.get() != self.conf_password_entry.get():
            messagebox.showerror("Error", "Password & Confirm Password must be same")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="_Sudhanshu9.", database="face_recognizer")
            my_cursor = conn.cursor()
            query = ("select * from register where email=%s")
            value = (self.email_entry.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror("Error", "User already exist, please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",
                                  (
                                      self.fname_entry.get(),
                                      self.lname_entry.get(),
                                      self.contact_entry.get(),
                                      self.email_entry.get(),
                                      self.combo_security_Q.get(),
                                      self.security_A_entry.get(),
                                      self.password_entry.get()
                                  ))

            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Register Successfully")

if __name__ == "__main__":
    main()