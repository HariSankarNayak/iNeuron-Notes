#  Age calculator using Tkinter
from tkinter import *
from tkinter import messagebox

from datetime import date

f1 = Tk()
f1.title("Age Calculator")
f1.geometry("470x250+500+400")
f1.configure(bg="lightblue1")
f1.resizable(False, False)


def calculate():
    e5.delete(0,END)
    today = date.today()
    name = str(e1.get())
    year1= int(e2.get())
    month1=int(e3.get())
    date1=int(e4.get())
    birthdate = date(year1, month1, date1)
    age = today.year - birthdate.year
    if today.month < birthdate.month or today.month == birthdate.month and today.day < birthdate.day:
        age+= 1
    e5.insert(0,int(age))

def clear():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)


def exit():
    result = messagebox.askquestion("Exit", "Are You Sure You Want to Exit?")
    if result == "yes":
        f1.destroy()
    else:
        return None

l6 = Label(f1, text="Age calculator ", font="arial 18 bold",bg="dodgerblue2",borderwidth=10,width=25, relief="groove", anchor="center")
l6.grid(row=1, column=0, columnspan=3, sticky=E+W)

l1 = Label(f1, text="Name ", font="arial 16 bold", bg="deep sky blue", width=15, relief="groove", anchor="w")
l1.grid(row=2, column=0, columnspan=1, sticky=W)
e1 = Entry(f1, font="arial 16 bold", borderwidth=2, width=17, relief="sunken")
e1.grid(row=2, column=1, columnspan=2, sticky=W)

l2 = Label(f1, text="Year ", font="arial 16 bold", bg="deep sky blue", width=15, relief="groove", anchor="w")
l2.grid(row=3, column=0, columnspan=1, sticky=W)
e2 = Entry(f1, font="arial 16 bold", borderwidth=2, width=17, relief="sunken")
e2.grid(row=3, column=1, columnspan=1, sticky=W)

l3 = Label(f1, text="Month ", font="arial 16 bold", bg="deep sky blue", width=15, relief="groove", anchor="w")
l3.grid(row=4, column=0, columnspan=1, sticky=W)
e3 = Entry(f1, font="arial 16 bold", borderwidth=2, width=17, relief="sunken")
e3.grid(row=4, column=1, columnspan=1, sticky=W)

l4 = Label(f1, text="Date ", font="arial 16 bold", bg="deep sky blue", width=15, relief="groove", anchor="w")
l4.grid(row=5, column=0, columnspan=1, sticky=W)
e4 = Entry(f1, font="arial 16 bold", borderwidth=2, width=17, relief="sunken")
e4.grid(row=5, column=1, columnspan=1, sticky=W)

l5 = Label(f1, text="Age is  ", font="arial 16 bold", bg="deep sky blue", width=15, relief="groove", anchor="w")
l5.grid(row=6, column=0, columnspan=1, sticky=W)
e5 = Entry(f1, font="arial 16 bold", borderwidth=2, width=17, relief="sunken")
e5.grid(row=6, column=1, columnspan=1, sticky=W)

b1 = Button(text="Calculate", font="arial 16 bold", bg="light yellow", command=calculate)
b1.grid(row=9, column=0, columnspan=1)

b2 = Button(text="Clear", font="arial 16 bold", bg="light yellow", command=clear)
b2.grid(row=9, column=1, columnspan=1)

b3 = Button(text="Exit", font="arial 16 bold", bg="light yellow", command=exit)
b3.grid(row=9, column=2, columnspan=1)

f1.mainloop()
