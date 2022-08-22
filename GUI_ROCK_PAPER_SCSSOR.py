import random
import tkinter

from setuptools import Command

screen=tkinter.Tk()
screen.title("ROCK PAPER SCISSOR")
screen.geometry("500x470")
var_user_choice=tkinter.StringVar()
var_com_choice=tkinter.StringVar()
var_result_choice=tkinter.StringVar()
screen.configure(bg="grey")

game_list=["ROCK","PAPER","SCISSOR"]
c=0
d=0
def myfun(msg):
    var_user_choice.set(msg)
    com=random.choice(game_list)
    var_com_choice.set(com)

    if msg==com:
        var_result_choice.set("TIE")
    else:
        if msg=="ROCK" and com=="PAPER" or msg=="PAPER" and com=="SCISSOR" or msg=="SCISSOR" and com=="ROCK":
            var_result_choice.set("COMPUTER WON")
           
            while True:
                global c
                c=c+1 
                var_display.set(c)
                break

        else:
            var_result_choice.set("USER WIN")

            while True:
                global d
                d=d+1 
                var_display1.set(d)
                break
            
var_display=tkinter.StringVar()
var_display1=tkinter.StringVar()








btn=tkinter.Button(screen,text="ROCK",font=("arial",20,"bold"),bg="blue",fg="orange",activebackground="black",activeforeground="white",command=lambda:myfun("ROCK"))
btn.place(x=25,y=10)

btn=tkinter.Button(screen,text="PAPER",font=("arial",20,"bold"),bg="blue",fg="orange",activebackground="black",activeforeground="white",command=lambda:myfun("PAPER"))
btn.place(x=180,y=10)

btn=tkinter.Button(screen,text="SCISSOR",font=("arial",20,"bold"),bg="blue",fg="orange",activebackground="black",activeforeground="white",command=lambda:myfun("SCISSOR"))
btn.place(x=330,y=10)
user=tkinter.Label(screen,text="USER",font=("arial",14,"bold"),bg="pink")
user.place(x=10,y=150)
user=tkinter.Label(screen,textvariable=var_display1,font=("arial",14,"bold"),bg="orange")
user.place(x=350,y=150)
computer=tkinter.Label(screen,text="COMPUTER",font=("arial",14,"bold"),bg="pink")
computer.place(x=10,y=180)
user=tkinter.Label(screen,textvariable=var_display,font=("arial",14,"bold"),bg="orange")
user.place(x=350,y=180)

user=tkinter.Label(screen,textvariable=var_user_choice,font=("arial",14,"bold"))
user.place(x=150,y=150)
computer=tkinter.Label(screen,textvariable=var_com_choice,font=("arial",14,"bold"))
computer.place(x=150,y=180)
btn=tkinter.Button(screen,textvariable=var_result_choice,font=("arial",20,"bold"),bg="violet",fg="black",activebackground="black",activeforeground="white",width="28")
btn.place(x=10,y=400)


screen.mainloop()