from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkvideo import tkvideo
from PIL import Image, ImageTk
from student import Student
from contact import Contact

import mysql.connector
import cv2
import threading
import subprocess


class Facial_Recognition_System:
    def __init__(self, root):  # root - window name
        self.root = root  # initialize self
        self.root.geometry("1530x790+0+0")  # set geometry of the window
        self.root.title("Facial Recognition System")

        # Load and set the background image
        img = Image.open(r"EvoSense_login\\assets\\img\\bg.jpg")
        img = img.resize((1300, 700), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, width=1300, height=700)

        # Load and play the background video
        bg_vid = Label(self.root)
        bg_vid.pack()
        player = tkvideo("EvoSense_login\\assets\\video\\tech_bg_vid.mp4", bg_vid, loop=1, size=(1300, 700))
        player.play()
        
        # Title Label
        title_lbl = Label(self.root, text="Facial Recognition", font=("Times New Roman", 35, "bold"), bg="black", fg="#74a7d2")
        title_lbl.place(x=0, y=0, width=1300, height=60)

        # Student button
        img2 = Image.open(r"EvoSense_login\\assets\\img\\student_button.jpg")
        img2 = img2.resize((220, 220), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        b1 = Button(self.root, image=self.photoimg2, command=self.student_details, cursor="hand2")
        b1.place(x=100, y=100, width=220, height=220)

        b2 = Button(self.root, text="Student Details", command=self.student_details, cursor="hand2", font=("Times New Roman", 15, "bold"), bg="black", fg="white")
        b2.place(x=100, y=300, width=220, height=40)

        # Face detection button
        img3 = Image.open(r"EvoSense_login\\assets\\img\\face_id_button.jpg")
        img3 = img3.resize((220, 220), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        b1 = Button(self.root, image=self.photoimg3, cursor="hand2", command=self.face_recog)
        b1.place(x=530, y=100, width=220, height=220)

        b2 = Button(self.root, text="Face Detector", cursor="hand2", command=self.face_recog, font=("Times New Roman", 15, "bold"), bg="black", fg="white")
        b2.place(x=530, y=300, width=220, height=40)

        # Exit button
        img5 = Image.open(r"EvoSense_login\\assets\\img\\exit.jpg")
        img5 = img5.resize((100, 100), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(self.root, image=self.photoimg5, cursor="hand2", command=self.exit_func)
        b1.place(x=580, y=455, width=100, height=100)

        b2 = Button(self.root, text="Exit", cursor="hand2", command=self.exit_func, font=("Times New Roman", 15, "bold"), bg="black", fg="white")
        b2.place(x=580, y=545, width=100, height=20)

        # Contact button
        img6 = Image.open(r"EvoSense_login\\assets\\img\\help_desk.jpg")
        img6 = img6.resize((220, 220), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(self.root, image=self.photoimg6, cursor="hand2", command=self.contact)
        b1.place(x=950, y=100, width=220, height=220)

        b2 = Button(self.root, text="Contact", cursor="hand2", command=self.contact, font=("Times New Roman", 15, "bold"), bg="black", fg="white")
        b2.place(x=950, y=300, width=220, height=40)

        # for face recognition
        self.assistant_opened = False

    # Exit function
    def exit_func(self):
        self.exit_func = messagebox.askyesno("Exit", "Do you really want to exit?")
        if self.exit_func > 0:
            self.root.destroy()
        else:
            return

    # Function Buttons
    def contact(self):
        self.new_window = Toplevel(self.root)
        self.app = Contact(self.new_window)

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    # Face Recognition
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbours, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbours)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), color, 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100 * (1 - (predict / 300))))

                conn = mysql.connector.connect(host="localhost", username="root", password="_Sudhanshu9.", database="face_recognizer")
                my_cursor = conn.cursor()

                my_cursor.execute("SELECT Name FROM student WHERE Student_Id="+str(id))
                n = my_cursor.fetchone()
                n = "+".join(n)

                my_cursor.execute("SELECT Roll FROM student WHERE Student_Id="+str(id))
                r = my_cursor.fetchone()
                r = "+".join(r)

                my_cursor.execute("SELECT Dep FROM student WHERE Student_Id="+str(id))
                d = my_cursor.fetchone()
                d = "+".join(d)

                if confidence > 87:
                    cv2.putText(img, f"Roll:{r}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name:{n}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department:{d}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, "Face Authenticated", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    cv2.imshow("Welcome to Face Recognition", img)
                    cv2.waitKey(1000)

                    if not self.assistant_opened:
                        threading.Thread(target=self.open_virtual_assistant).start()
                        self.assistant_opened = True
                        # Call the run.py script
                        subprocess.Popen(["python", "run.py"])

                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, h]
            
            return coord
        
        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img
        
        faceCascade = cv2.CascadeClassifier("EvoSense_login\\haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition", img)
            
            if cv2.waitKey(1) == 13 or self.assistant_opened == True:
                break

        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = Facial_Recognition_System(root)
    root.mainloop()
