import tkinter as tk
from tkinter import *
import os, cv2
import shutil
import csv
import numpy as np
from PIL import ImageTk, Image
import pandas as pd
import datetime
import time
import tkinter.font as font
import pyttsx3

# project module
import show_attendance
import takeImage
import trainImage
import automaticAttedance
import update_student_details

# Function to convert text to speech
def text_to_speech(user_text):
    engine = pyttsx3.init()
    engine.say(user_text)
    engine.runAndWait()

# Path definitions
haarcasecade_path = "D:\\Attendance\\haarcascade_frontalface_default.xml"
trainimagelabel_path = "D:\\Attendance\\TrainingImageLabel\\Trainner.yml"
trainimage_path = "D:\\Attendance\\TrainingImage"
studentdetail_path = "D:\\Attendance\\StudentDetails\\studentdetails.csv"
attendance_path = "D:\\Attendance\\Attendance"

# Create the main window
window = Tk()
window.title("Face recognition")
# window.geometry("1280x720")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry(str(screen_width) + "x" + str(screen_height))
window.resizable(False,False)
dialog_title = "QUIT"
dialog_text = "Are you sure want to close?"
window.configure(background="#223039")
ico = tk.PhotoImage(file="UI_Image\\Face Recognition Logo.png")
window.iconphoto(False, ico)

# Function to destroy warning screen
def del_sc1():
    sc1.destroy()

# Function to display error screen
def err_screen():
    global sc1
    sc1 = tk.Tk()
    sc1.geometry("400x110")
    sc1.iconbitmap("AMS.ico")
    sc1.title("Warning!!")
    sc1.configure(background="#223039")
    sc1.resizable(0, 0)
    tk.Label(
        sc1,
        text="Enrollment & Name required!!!",
        fg="#D5A952",
        bg="#223039",
        font=("times", 20, " bold "),
    ).pack()
    tk.Button(
        sc1,
        text="OK",
        command=del_sc1,
        fg="#D5A952",
        bg="#223039",
        width=9,
        height=1,
        activebackground="Red",
        font=("times", 20, " bold "),
    ).place(x=110, y=50)

# Function to validate input
def testVal(inStr, acttyp):
    if acttyp == "1":  # insert
        if not inStr.isdigit():
            return False
    return True

# Create labels and buttons
titl = tk.Label(window, bg="#223039", relief=RIDGE, bd=10, font=("Ubuntu", 35))
titl.pack(fill=X)

titl = tk.Label(
    window, text="RV University ", bg="#223039", fg="#D5A952", font=("Ubuntu", 27),
)
titl.place(x=655, y=12) 

a = tk.Label(
    window,
    text="Smart Attendance System",
    bg="#223039",
    fg="#D5A952",
    bd=10,
    font=("Ubuntu", 35),
)
a.pack()

# Images
ri = Image.open("UI_Image/register.png")
ri = ri.resize((225, 225))
r = ImageTk.PhotoImage(ri)
label1 = Label(window, image=r)
label1.image = r
label1.place(x=100, y=270)

ai = Image.open("UI_Image/attendance.png")
ai = ai.resize((225, 225))
a = ImageTk.PhotoImage(ai)
label2 = Label(window, image=a)
label2.image = a
label2.place(x=1200, y=270)

vi = Image.open("UI_Image/verifyy.png")
vi = vi.resize((225, 225))
v = ImageTk.PhotoImage(vi)
label3 = Label(window, image=v)
label3.image = v
label3.place(x=655, y=270)

# Function to open image capture UI
def TakeImageUI():
    ImageUI = Tk()
    ImageUI.title("Take Student Image..")
    ImageUI.geometry("780x480")
    ImageUI.configure(background="#223039")
    ImageUI.resizable(0, 0)
    titl = tk.Label(ImageUI, bg="#223039", relief=RIDGE, bd=10, font=("Ubuntu", 35))
    titl.pack(fill=X)

    titl = tk.Label(
        ImageUI, text="Register Your Face", bg="#223039", fg="#D5A952", font=("Ubuntu", 30),
    )
    titl.place(x=270, y=12)

    a = tk.Label(
        ImageUI,
        text="Enter the details",
        bg="#223039",
        fg="#D5A952",
        bd=10,
        font=("Ubuntu", 24),
    )
    a.place(x=280, y=75)

    lbl1 = tk.Label(
        ImageUI,
        text="Enrollment No",
        width=10,
        height=2,
        bg="#223039",
        fg="#D5A952",
        bd=5,
        relief=RIDGE,
        font=("times new roman", 12),
    )
    lbl1.place(x=120, y=130)
    txt1 = tk.Entry(
        ImageUI,
        width=17,
        bd=5,
        bg="#223039",
        fg="#D5A952",
        relief=RIDGE,
        font=("times", 25, "bold"),
    )
    txt1.place(x=250, y=130)
    txt1["validatecommand"] = (txt1.register(testVal), "%P", "%d")

    lbl2 = tk.Label(
        ImageUI,
        text="Name",
        width=10,
        height=2,
        bg="#223039",
        fg="#D5A952",
        bd=5,
        relief=RIDGE,
        font=("times new roman", 12),
    )
    lbl2.place(x=120, y=200)
    txt2 = tk.Entry(
        ImageUI,
        width=17,
        bd=5,
        bg="#223039",
        fg="#D5A952",
        relief=RIDGE,
        font=("times", 25, "bold"),
    )
    txt2.place(x=250, y=200)

    lbl3 = tk.Label(
        ImageUI,
        text="Notification",
        width=10,
        height=2,
        bg="#223039",
        fg="#D5A952",
        bd=5,
        relief=RIDGE,
        font=("times new roman", 12),
    )
    lbl3.place(x=120, y=270)

    message = tk.Label(
        ImageUI,
        text="",
        width=32,
        height=2,
        bd=5,
        bg="#223039",
        fg="#D5A952",
        relief=RIDGE,
        font=("times", 12, "bold"),
    )
    message.place(x=250, y=270)

    def take_image():
        l1 = txt1.get()
        l2 = txt2.get()
        takeImage.TakeImage(
            l1,
            l2,
            haarcasecade_path,
            trainimage_path,
            message,
            err_screen,
            text_to_speech,
        )
        txt1.delete(0, "end")
        txt2.delete(0, "end")

    takeImg = tk.Button(
        ImageUI,
        text="Take Image",
        command=take_image,  # Updated to call take_image function
        bd=10,
        font=("times new roman", 18),
        bg="#223039",
        fg="#D5A952",
        height=2,
        width=12,
        relief=RIDGE,
    )
    takeImg.place(x=130, y=350)

    def train_image():
        trainImage.TrainImage(
            haarcasecade_path,
            trainimage_path,
            trainimagelabel_path,
            message,
            text_to_speech,
        )

    trainImg = tk.Button(
        ImageUI,
        text="Train Image",
        command=train_image,
        bd=10,
        font=("times new roman", 18),
        bg="#223039",
        fg="#D5A952",
        height=2,
        width=12,
        relief=RIDGE,
    )
    trainImg.place(x=360, y=350)

    student_details = update_student_details.extract_student_details(trainimage_path)

    update_student_details.save_student_details_to_csv(student_details)

r = tk.Button(
    window,
    text="Register a new student",
    command=TakeImageUI,
    bd=10,
    font=("times new roman", 16),
    bg="#223039",
    fg="#D5A952",
    height=2,
    width=17,
)
r.place(x=100, y=520)


def automatic_attedance():
    automaticAttedance.subjectChoose(text_to_speech)


r = tk.Button(
    window,
    text="Take Attendance",
    command=automatic_attedance,
    bd=10,
    font=("times new roman", 16),
    bg="#223039",
    fg="#D5A952",
    height=2,
    width=17,
)
r.place(x=655, y=520)


def view_attendance():
    show_attendance.subjectchoose(text_to_speech)


r = tk.Button(
    window,
    text="View Attendance",
    command=view_attendance,
    bd=10,
    font=("times new roman", 16),
    bg="#223039",
    fg="#D5A952",
    height=2,
    width=17,
)
r.place(x=1200, y=520)
r = tk.Button(
    window,
    text="EXIT",
    bd=10,
    command=quit,
    font=("times new roman", 16),
    bg="#223039",
    fg="#D5A952",
    height=2,
    width=17,
)
r.place(x=655, y=690)

window.mainloop()
