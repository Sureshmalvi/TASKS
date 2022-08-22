from calendar import c
import tkinter
from tkinter.font import BOLD
from turtle import Screen

from setuptools import Command
Screen=tkinter.Tk()
Screen.geometry("550x550")
Screen.configure(bg="lightgreen")
var_like=tkinter.StringVar()
var_dislike=tkinter.StringVar()
var_choice=tkinter.StringVar()
var_display=tkinter.StringVar()
c=0
def like(msg):
    while True:
        global c
        c=c+1 
        print(var_display.set(f"Thank You For Like ({c}) "))
        break
d=0
def dislike(msg):
    while True:
        global d
        d=d+1 
        print(var_display.set(f"Thank You For Dislike ({d})"))
        break
def choice(msg):
    if msg=="like":
        var_choice.set("like")
        like("like")
    else:
        if msg=="dislike":
            var_choice.set("dislike")
            dislike("dislike")

lbl=tkinter.Label(Screen,text="Welcome To Youtube",font=("arial",26,"bold"),bg="lightgreen")
lbl.place(x=120,y=10)
btn=tkinter.Button(Screen,text="Like",font=("arial",20,"bold"),bg="yellow",command= lambda msg="like":like(msg))
btn.place(x=200,y=80)
btn=tkinter.Button(Screen,text="Dislike",font=("arial",20,"bold"),bg="yellow",command= lambda msg="dislike":choice(msg))
btn.place(x=300,y=80)
lbl=tkinter.Label(Screen, textvariable=var_like,font=("arial",26,"bold"),bg="lightgreen")
lbl.place(x=125,y=250)
lbl=tkinter.Label(Screen,font=("arial",26,"bold"),bg="lightgreen")
lbl.place(x=20,y=200)
btn=tkinter.Label(Screen,textvariable=var_display, font=("arial",20,"bold"),bg="yellow")
btn.place(x=130,y=200)
Screen.mainloop()
