from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2   #open computer vision library for object recognition
import os
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root,text="TRAIN DATA SET", font=("times new roman",35,"bold"),bg="white",fg="red") 
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top = Image.open(r"C:\Users\Dell\Proj\PROJECT\college_images\facialrecognition.png")
        img_top = img_top.resize((1530, 325), Image.ANTIALIAS if 'ANTIALIAS' in dir(Image) else Image.BICUBIC)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl3 = Label(self.root, image=self.photoimg_top)
        f_lbl3.place(x=0, y=55, width=1530, height=325)

        # button
        b1_1 = Button(self.root,text = "TRAIN DATA",command=self.train_classifier, cursor="hand2",font=("times new roman",30,"bold"),bg="blue",fg="white")
        b1_1.place(x=0,y=380,width=1530,height=60)


        img_bottom = Image.open(r"C:\Users\Dell\Proj\PROJECT\college_images\face-recognition.png")
        img_bottom = img_bottom.resize((1530, 325), Image.ANTIALIAS if 'ANTIALIAS' in dir(Image) else Image.BICUBIC)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl3 = Label(self.root, image=self.photoimg_bottom)
        f_lbl3.place(x=0, y=440, width=1530, height=325)

    def train_classifier(self):  # Define train_classifier method inside the Train class
        data_dir = ("data")
        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')   # Convert image to grayscale
            imageNp = np.array(img,'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) == 13 # press enter to close the window
        ids = np.array(ids)

        # ==================Train the clssifier dat=======================
        print("Training classifier...")
        clf=cv2.face.LBPHFaceRecognizer_create()  # For OpenCV 4.x and later
        clf.train(faces, ids)
        clf.write("classifier.xml")
        print("Training completed!")
        messagebox.showinfo("Result", "Training dataset completed!")

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
