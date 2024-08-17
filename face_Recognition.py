from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import time
import cv2
import os
import numpy as np

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root,text="FACE RECOGNITION", font=("times new roman",35,"bold"),bg="white",fg="purple") 
        title_lbl.place(x=0,y=0,width=1530,height=45)

        # 1st image
        img_top = Image.open(r"c:\Users\Dell\Desktop\college_images\face_detector1.jpg")
        img_top = img_top.resize((650, 700), Image.ANTIALIAS if 'ANTIALIAS' in dir(Image) else Image.BICUBIC)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl3 = Label(self.root, image=self.photoimg_top)
        f_lbl3.place(x=0, y=55, width=650, height=700)

        # 2nd image
        img_bottom = Image.open(r"c:\Users\Dell\Desktop\college_images\facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
        img_bottom = img_bottom.resize((950, 700), Image.ANTIALIAS if 'ANTIALIAS' in dir(Image) else Image.BICUBIC)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl3 = Label(self.root, image=self.photoimg_bottom)
        f_lbl3.place(x=650, y=55, width=950, height=700)

        # button
        b1_1 = Button(f_lbl3,text="Face Recognition", cursor="hand2",font=("times new roman",18,"bold"),bg="orange",fg="dark blue", command=self.face_recog)
        b1_1.place(x=370,y=625,width=200,height=40)

    #====================attendence=========================
    def mark_attendance(self, i, r, n, d):
        print("Marking attendance for:", i, r, n, d) 
        try:
            with open(r"Attendance.csv", "r+", newline="\n") as f:
                f.seek(0)
                myDataList = f.readlines()
                name_list = []
                for line in myDataList:
                    entry = line.split((","))
                    name_list.append(entry[0])

                if ((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                    now = datetime.now()
                    dtString = now.strftime("%H:%M:%S")
                    formatted_date = now.strftime("%m/%d/%Y")  # Format date as "mm/dd/yyyy"
                    # d1 = now.strftime("%d/%m/%Y")
                    # dtString=now.strftime("%H:%M:%S")
                
                    # f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")
                    f.writelines(f"\n{i},{r},{n},{d},{dtString},{formatted_date},Present")
                    print("Attendance marked successfully:", i, r, n, d)

        except Exception as e:
            print("Error marking attendance:", e)
        
    #===================face recognition================================
    def face_recog(self):
        def draw_boundray(img, classifier,scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image,scaleFactor, minNeighbors)

            coord = []
            
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100*(1-predict/300)))

                # Print the predicted ID for debugging
                print("Predicted ID:", id)

                conn=mysql.connector.connect(host="localhost", username="root",password="RSSBsim26@tu#",database="project")
                my_cursor=conn.cursor()

                my_cursor.execute("select Name from student where Student_id="+str(id))
                n = my_cursor.fetchone()
                if n is not None:
                    n = "+".join(n)

                my_cursor.execute("select Roll from student where Student_id=" + str(id))
                r = my_cursor.fetchone()
                if r is not None:
                    r = "+".join(r)

                my_cursor.execute("select Dep from student where Student_id=" + str(id))
                d = my_cursor.fetchone()
                if d is not None:
                    d = "+".join(d)
                
                my_cursor.execute("select Student_id from student where Student_id=" + str(id))
                i = my_cursor.fetchone()
                if i is not None:
                    i = "+".join(i)

                if confidence>70:
                    conn = mysql.connector.connect(host="localhost", username="root", password="RSSBsim26@tu#", database="project")
                    my_cursor = conn.cursor()

                    my_cursor.execute("select Name, Roll, Dep, Student_id from student where Student_id=" + str(id))
                    result = my_cursor.fetchone()
                    if result is not None:
                        n, r, d, i = result
                        self.mark_attendance(i, r, n, d) 
                        print("Attendance marked successfully:", i, r, n, d)  

          
                    cv2.putText(img, f"ID:{i}", (x,y-80), cv2.FONT_HERSHEY_COMPLEX, 0.8,(127,0,255), 2)
                    cv2.putText(img, f"Roll:{r}", (x,y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8,(127,0,255), 2)
                    cv2.putText(img, f"Name:{n}", (x,y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8,(127,0,255), 2)
                    cv2.putText(img, f"Department:{d}", (x,y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8,(127,0,255), 2)
             
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(127,0,255),2)
                    cv2.putText(img,f"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX, 0.8, (127,0,255),2)

                coord = [x,y,w,y]   ##

            return  coord
        
        def recognize(img,clf,faceCascade):
            coord = draw_boundray(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
            
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret,img = video_cap.read()
            img = recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recognition",img)

            if cv2.waitKey(1) == 13:  # Break the loop if 'Enter' key is pressed
                break
        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
