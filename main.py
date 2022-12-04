import string
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image

root = Tk()
root.title("BMI")
root.geometry("1080x720")
img=Image.open( "health.jpg")
bc=ImageTk.PhotoImage(img)


root.geometry("600x600")
lbl=Label(root,image=bc,anchor=CENTER)
lbl.place(x=0,y=0)
def bmi():
    height=h.get()
    weight=w.get()
    lbl.configure(text=string)
    print(height)
    print(weight)
    calculate_bmi()

def calculate_bmi():
    kg = int(w.get())
    m = int(h.get())/100
    bmi = kg/(m*m)
    bmi = round(bmi, 1)
    bmi_index(bmi)

def bmi_index(bmi):
    
    if bmi < 18.5:
        messagebox.showinfo('bmi-pythonguides', f'BMI = {bmi} is Underweight')
    elif (bmi > 18.5) and (bmi < 24.9):
        messagebox.showinfo('bmi-pythonguides', f'BMI = {bmi} is Normal')
    elif (bmi > 24.9) and (bmi < 29.9):
        messagebox.showinfo('bmi-pythonguides', f'BMI = {bmi} is Overweight')
    elif (bmi > 29.9):
        messagebox.showinfo('bmi-pythonguides', f'BMI = {bmi} is Obesity') 
    else:
        messagebox.showerror('bmi-pythonguides', 'something went wrong!') 

h1 = Label(text="Height")
h1.place(x=40,y=60)

w1 = Label(text="Weigth")
w1.place(x=40,y=100)

submit_button = Button(text="Submit",command=bmi).place(x=40,y=140)

h= Entry(root,width=15)
h.place(x=110,y=60)

w = Entry(root,width=15)
w.place(x=110,y=100)


root.mainloop()
