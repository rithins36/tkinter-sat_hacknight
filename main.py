import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("BMI")
root.geometry("1080x720")
img=Image.open( "health.jpg")
bc=ImageTk.PhotoImage(img)


root.geometry("800x600")
lbl=Label(root,image=bc,anchor=CENTER).place(x=0,y=0)
def bmi():
    height=h.get()
    weight=w.get()
    lbl.configure(text=string)
    print(height)
    print(weight)

h1 = Label(text="Height").place(x=40,
                                         y=60)

# the label for user_password
w1 = Label(text="Weigth").place(x=40,
                                             y=100)

submit_button = Button(
                       text="Submit",command=bmi).place(x=40,
                                            y=130)

h= Entry(
                             width=15).place(x=110,
                                             y=60)

w = Entry(
                                 width=15).place(x=110,
                                                 y=100)


root.mainloop()
