import sys
from tkinter import *
import time
import datetime as dt


def times():
    current_time=time.strftime("%H:%M:%S")
    clock.config(text=current_time)
    clock.after(200,times)


root  = Tk()
root.geometry("460x250")
root.title("Digital Clock")
root.configure(bg='yellow')
digi = Label(root,text="Digital Clock",font="times 24 bold")
digi.grid(row=0,column=2)

clock=Label(root,font=("times",50,"bold"),background='green',foreground='white')
clock.grid(row=2,column=2,pady=25,padx=100)
times()


date = dt.datetime.now()
#print(date)
label = Label(root, text=f"{date :%A, %B %d, %Y}", font="Calibri, 20")
label.grid(row=3,column=2)

root.mainloop()