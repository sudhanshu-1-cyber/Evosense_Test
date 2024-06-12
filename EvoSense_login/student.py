from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import numpy as np
import os

class Student:
    def __init__(self, root):       #root -  window name     
        self.root=root          #initialize self
        self.root.geometry("1530x790+0+0") #set geometary of the window
        self.root.title("Facial Recognition System")

        # --------------Variables-----------------
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_dep=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()

        # bg image
        img=Image.open(r"EvoSense_login\\assets\\img\\bg.jpg")
        img=img.resize((1300, 700), Image.ADAPTIVE)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, width=1300, height=700)

        title_lbl=Label(bg_img, text="Student Details", font=("Times New Roman",28,"bold"),bg="black", fg="#74a7d2")
        title_lbl.place(x=0, y=0, width=1300, height=45)

        main_frame=Frame(bg_img, bd = 2, bg = "white")
        main_frame.place(x=20, y=50, width=1225, height=620)

        #left label frame

        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 13, "bold"))
        Left_frame.place(x=10, y=10, width=600, height=580)

        img_left=Image.open(r"EvoSense_login\\assets\\img\\bg.jpg")
        img_left=img_left.resize((1300, 700), Image.ADAPTIVE) 
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        bg_img=Label(Left_frame, image=self.photoimg_left)
        bg_img.place(x=5, y=0, width=585, height=130)


        #current course
        current_course_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Current course information", font=("times new roman", 13, "bold"))
        current_course_frame.place(x=5, y=135, width=585, height=115)

        # Department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman", 12, "bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman", 12, "bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Department","Computer","IT","Civil","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        # Course
        course_label=Label(current_course_frame,text="Course",font=("times new roman", 12, "bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman", 12, "bold"),width=17,state="readonly")
        course_combo["values"]=("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        # Year
        year_label=Label(current_course_frame,text="Year",font=("times new roman", 12, "bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman", 12, "bold"),width=17,state="readonly")
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        # Semester
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman", 12, "bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman", 12, "bold"),width=17,state="readonly")
        semester_combo["values"]=("Select Semester","Semester-1","Semester-2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        # Class Student information
        class_student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Class Student information", font=("times new roman", 13, "bold"))
        class_student_frame.place(x=5, y=250, width=585, height=300)

        # student ID
        studentId_label=Label(class_student_frame,text="Student ID:",font=("times new roman", 12, "bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentId_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=17,font=("times new roman", 12, "bold"))
        studentId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        # student name
        studentName_label=Label(class_student_frame,text="Student Name:",font=("times new roman", 12, "bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=17,font=("times new roman", 12, "bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        # class division
        class_div_label=Label(class_student_frame,text="Class Division:",font=("times new roman", 12, "bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        class_div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman", 12, "bold"),width=15,state="readonly")
        class_div_combo["values"]=("A","B","C","D")
        class_div_combo.current(0)
        class_div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        # Roll no
        roll_no_label=Label(class_student_frame,text="Roll No:",font=("times new roman", 12, "bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=17,font=("times new roman", 12, "bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        # Gender
        gender_label=Label(class_student_frame,text="Gender:",font=("times new roman", 12, "bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman", 12, "bold"),width=15,state="readonly")
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        # DOB
        dob_label=Label(class_student_frame,text="DOB:",font=("times new roman", 12, "bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=17,font=("times new roman", 12, "bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        # Email
        email_label=Label(class_student_frame,text="Email:",font=("times new roman", 12, "bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=17,font=("times new roman", 12, "bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        # phone no
        phone_label=Label(class_student_frame,text="Phone No:",font=("times new roman", 12, "bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=17,font=("times new roman", 12, "bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        # Address
        address_label=Label(class_student_frame,text="Address:",font=("times new roman", 12, "bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=17,font=("times new roman", 12, "bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        # Teacher Name
        teacher_label=Label(class_student_frame,text="Teacher Name:",font=("times new roman", 12, "bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=17,font=("times new roman", 12, "bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        # Radio buttons
        self.var_radio=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=0)

        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio,text="No Photo Sample",value="No")
        radiobtn2.grid(row=6,column=1)

        # Button frame 1
        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=1,y=200,width=575,height=35)

        # save button
        save_btn=Button(btn_frame1,text="Save",command=self.add_data,width=15,font=("times new roman", 12, "bold"),bg="#152e43",fg="white")
        save_btn.grid(row=0,column=0)

        # update button
        update_btn=Button(btn_frame1,text="Update",command=self.update_data,width=15,font=("times new roman", 12, "bold"),bg="#152e43",fg="white")
        update_btn.grid(row=0,column=1)

        # delete button
        delete_btn=Button(btn_frame1,text="Delete",command=self.delete_data,width=15,font=("times new roman", 12, "bold"),bg="#152e43",fg="white")
        delete_btn.grid(row=0,column=2)

        # reset button
        reset_btn=Button(btn_frame1,text="Reset",command=self.reset_data,width=15,font=("times new roman", 12, "bold"),bg="#152e43",fg="white")
        reset_btn.grid(row=0,column=3)


        # Button frame 2
        btn_frame2=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame2.place(x=1,y=235,width=575,height=35)

        # take photo button
        take_photo_btn=Button(btn_frame2,command=self.generate_dataset,text="Take Photo Sample",width=31,font=("times new roman", 12, "bold"),bg="#152e43",fg="white")
        take_photo_btn.grid(row=0,column=0)

        # confirm photo button
        take_photo_btn=Button(btn_frame2,command=self.train_classifier,text="Confirm Photo Sample",width=31,font=("times new roman", 12, "bold"),bg="#152e43",fg="white")
        take_photo_btn.grid(row=0,column=1)

        
        # Right label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Record", font=("times new roman", 13, "bold"))
        Right_frame.place(x=615, y=10, width=600, height=580)

        img_right=Image.open(r"EvoSense_login\\assets\\img\\bg.jpg")
        img_right=img_right.resize((1300, 700), Image.ADAPTIVE) 
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        bg_img=Label(Right_frame, image=self.photoimg_right)
        bg_img.place(x=5, y=0, width=580, height=130)


        # Table Frame
        table_frame=LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=140, width=585, height=400)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("Dep","Course","Year","Sem","ID","Name","Div","Roll","Gender","DOB","Email","Phone","Address","Teacher","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Dep",text="Department")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Sem",text="Semester")
        self.student_table.heading("ID",text="StudentID")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Div",text="Division")
        self.student_table.heading("Roll",text="Roll No")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Phone",text="Phone No")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Teacher",text="Teacher")
        self.student_table.heading("Photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("Dep",width=120)
        self.student_table.column("Course",width=120)
        self.student_table.column("Year",width=120)
        self.student_table.column("Sem",width=120)
        self.student_table.column("ID",width=120)
        self.student_table.column("Name",width=120)
        self.student_table.column("Div",width=120)
        self.student_table.column("Roll",width=120)
        self.student_table.column("Gender",width=120)
        self.student_table.column("DOB",width=120)
        self.student_table.column("Email",width=120)
        self.student_table.column("Phone",width=120)
        self.student_table.column("Address",width=120)
        self.student_table.column("Teacher",width=120)
        self.student_table.column("Photo",width=120)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data() 



    
    # ----------------Function Declaration--------------


    # Train Data

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')  # Gray scale image 
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13

        ids=np.array(ids)


        # --------------- Train the classifier and save -------------
        clf=cv2.face.LBPHFaceRecognizer_create()    
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!")

    
    # Add student data
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_id.get()=="" or self.var_std_name.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="_Sudhanshu9.",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio.get()

                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)


    # -------------Fetch Data-----------
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="_Sudhanshu9.",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    # --------------Get Cursor------------
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio.set(data[14])

    # Update Function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_id.get()=="" or self.var_std_name.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update student details?",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="_Sudhanshu9.",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_ID=%s",
                    ( 
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio.get(),
                        self.var_std_id.get()

                    ))

                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Students details successfully updated!",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()

            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    # Delete Funtion
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student ID is required.",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to delete student details?",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="_Sudhanshu9.",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_ID=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Student details successfully deleted",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    # Reset Data
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio.set("")


    # ----------- Generate data set take photo samples ---------------
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_id.get()=="" or self.var_std_name.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="_Sudhanshu9.",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_ID=%s",
                    ( 
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio.get(),
                        self.var_std_id.get()==id+1

                    ))

                conn.commit()   
                self.fetch_data()
                self.reset_data()
                conn.close()

                # -------------- Load predifined data on face frontals from opencv -------------

                face_classifier=cv2.CascadeClassifier("EvoSense_login\\haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    # Scaling factor=1.3
                    # Minimum neighbour=5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==1000:
                        break

                cap.release()
                cv2.destroyAllWindows()

                messagebox.showinfo("Result","Generating data set completed!!!")
           
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

                
if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()