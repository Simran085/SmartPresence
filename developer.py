from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2   #open computer vision library for object recognition

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root,text="DEVELOPER", font=("times new roman",35,"bold"),bg="white",fg="Purple") 
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top = Image.open(r"C:\Users\Dell\Desktop\college_images\Devel.jpeg")
        img_top = img_top.resize((1530, 720), Image.ANTIALIAS if 'ANTIALIAS' in dir(Image) else Image.BICUBIC)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl3 = Label(self.root, image=self.photoimg_top)
        f_lbl3.place(x=0, y=55, width=1530, height=720)

        # Frame
        main_frame = Frame(f_lbl3,bd=2,bg="white")
        main_frame.place(x=1000,y=0,width=500,height=600)

        img_top1 = Image.open(r"C:\Users\Dell\Pictures\Camera Roll\woman-programmer.jpg")
        img_top1 = img_top1.resize((200, 200), Image.ANTIALIAS if 'ANTIALIAS' in dir(Image) else Image.BICUBIC)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

         #developer info
        dep_label = Label(main_frame,text="Hello! My name is Simran",font= ("times new roman", 19,"bold"),fg="Black",bg="white")
        dep_label.place(x=0, y=5)

         #developer info
        dep_label = Label(main_frame,text="I am a full stack developer.",font= ("times new roman", 19,"bold"),fg="Black", bg="white")
        dep_label.place(x=0, y=40)

        f_lbl3 = Label(main_frame, image=self.photoimg_top1)
        f_lbl3.place(x=300, y=0, width=200, height=200)

          # Third image
        img2 = Image.open(r"C:\Users\Dell\Desktop\college_images\KPIs-and-Agile-software-development-metrics-for-teams-1.jpg")
        img2 = img2.resize((500, 390), Image.ANTIALIAS if 'ANTIALIAS' in dir(Image) else Image.BICUBIC)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl3 = Label(main_frame, image=self.photoimg2)
        f_lbl3.place(x=0, y=210, width=500, height=390)

if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()