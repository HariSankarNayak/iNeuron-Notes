from tkinter import *
from tkinter import ttk, messagebox

def mycalc():
    weight = float(e1.get())
    milligram= weight * 1000000
    e2.insert(0, int(milligram))
    centigram= weight * 100000
    e3.insert(0, int(centigram))
    decigram= weight * 10000
    e4.insert(0, int(decigram))
    gram = weight * 1000
    e5.insert(0, int(gram))
    kilogram= weight * 1
    e6.insert(0, int(kilogram))
    ton= weight * 0.001
    e7.insert(0, float(ton))
    newton = weight * 9.807
    e8.insert(0, float(newton))
    b1.config(bg="green2")
    e1.focus()

def myclear():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)
    e8.delete(0, END)

    b1.config(bg="white smoke")

def myexit():
    result = messagebox.askquestion("Exit", "Are You Sure You Want to Exit?")
    if result == "yes":
        f1.destroy()
    else:
        return None

f1 = Tk()

f1.title("Weight Convertor ")
f1.geometry("480x250+300+300")
f1.resizable(False, False)

l1= Label(f1, text="Enter weight in kg", bg="plum1", fg="black", font="arial 12 bold", width=20, relief="sunken",anchor="w")
l2= Label(f1, text="Milligram", bg="tan1", fg="black", font="arial 12", width=22,  relief="sunken",anchor="w")
l3= Label(f1, text="Centigram", bg="tan1", fg="black", font="arial 12", width=22,relief="sunken", anchor="w")
l4 = Label(f1, text="Decigram", bg="tan1", fg="black", font="arial 12", width=22, relief="sunken", anchor="w")
l5 = Label(f1, text="Gram", bg="tan1", fg="black", font="arial 12", width=22, relief="sunken", anchor="w")
l6 = Label(f1, text="Kilogram", bg="tan1", fg="black", font="arial 12",width=22, relief="sunken", anchor="w")
l7 = Label(f1, text="Ton", bg="tan1", fg="black", font="arial 12", width=22, relief="sunken", anchor="w")
l8 = Label(f1, text="Newton", bg="tan1", fg="black", font="arial 12", width=22, relief="sunken", anchor="w")
l1.grid(row=0, column=0, columnspan=1, padx=0, ipady=0)
l2.grid(row=1, column=0, columnspan=1, padx=0, pady=0)
l3.grid(row=2, column=0, columnspan=1, padx=0, pady=0)
l4.grid(row=3, column=0, columnspan=1, padx=0, pady=0)
l5.grid(row=4, column=0, columnspan=1, padx=0, pady=0)
l6.grid(row=5, column=0, columnspan=1, padx=0, pady=0)
l7.grid(row=6, column=0, columnspan=1, padx=0, pady=0)
l8.grid(row=7, column=0, columnspan=1, padx=0, pady=0)

e1 = Entry(f1, font="arial 12 bold", borderwidth=2,bg="plum1")
e2 = Entry(f1, font="arial 12", borderwidth=2,bg="palegreen1")
e3 = Entry(f1, font="arial 12", borderwidth=2,bg="palegreen1")
e4 = Entry(f1, font="arial 12", borderwidth=2,bg="palegreen1")
e5 = Entry(f1, font="arial 12", borderwidth=2,bg="palegreen1")
e6 = Entry(f1, font="arial 12", borderwidth=2,bg="palegreen1")
e7 = Entry(f1, font="arial 12", borderwidth=2,bg="palegreen1")
e8 = Entry(f1, font="arial 12", borderwidth=2,bg="palegreen1")
e1.grid(row=0, column=1, columnspan=1, padx=0, pady=0)
e2.grid(row=1, column=1, columnspan=1, padx=0, pady=0)
e3.grid(row=2, column=1, columnspan=1, padx=0, pady=0)
e4.grid(row=3, column=1, columnspan=1, padx=0, pady=0)
e5.grid(row=4, column=1, columnspan=1, padx=0, pady=0)
e6.grid(row=5, column=1, columnspan=1, padx=0, pady=0)
e7.grid(row=6, column=1, columnspan=1, padx=0, pady=0)
e8.grid(row=7, column=1, columnspan=1, padx=0, pady=0)

b1 = Button(f1, text="Convert",  font="arial 10",command=mycalc)
b2 = Button(f1, text="Clear", font="arial 10", command=myclear)
b3 = Button(f1, text="Exit", font="arial 10", command=myexit)
b1.grid(row=10, column=0, columnspan=1, pady=0, padx=0, sticky=E + W)
b2.grid(row=10, column=1, columnspan=1, pady=0, padx=0, sticky=E + W)
b3.grid(row=10, column=2, columnspan=1, pady=0, ipadx=20, sticky=E + W)

f1.mainloop()
