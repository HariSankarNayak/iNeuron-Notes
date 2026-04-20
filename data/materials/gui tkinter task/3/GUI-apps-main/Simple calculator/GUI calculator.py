#  Simple GUI calculator using Tkinter
from tkinter import *

def input(num):
    temp = e1.get()
    e1.delete(0, END)
    e1.insert(0, temp + num)
    e1.focus()


def backspace():
    e1_len = len(e1.get())
    e1.delete(e1_len - 1)


def clear():
    e1.delete(0, END)


def get(operator):
    global num1, calc
    num1 = e1.get()
    calc = operator
    e1.insert(END, calc)
    try:
        num1 = float(num1)
    except ValueError:
        clear()

def calculate():
    input_1 = e1.get()
    num2 = float(input_1[input_1.index(calc) + 1:])  # 2nd num
    e1.delete(0, END)
    if calc == "+":
        e1.insert(0, str(num1 + num2))
    elif calc == "-":
        e1.insert(0, str(num1 - num2))
    elif calc == "x":
        e1.insert(0, str(num1 * num2))

    elif calc == "/":
        try:
            e1.insert(0, str(num1 / num2))
        except ZeroDivisionError:
            e1.insert(0, "Undefined")
    elif calc == "%":
        try:
            e1.insert(0, str(num1 / num2 * .01))
        except ZeroDivisionError:
            e1.insert(0, "Undefined")


f1 = Tk()

f1.title("Calculator")
f1.config(bg="black")
f1.geometry("396x283+600+400")
f1.resizable(False, False)

b_fun = "black"
b_num = "black"
b_fun1 = "white"
b_num1 = "white"

l1 = Label(f1, text="Standard calculator", fg="white", bg="black", font="arial 16", relief="flat")
l1.grid(row=0, column=0, columnspan=4, padx=0, pady=0, sticky=W + W)

e1 = Entry(f1, font="arial 20 bold", borderwidth=2)
e1.grid(row=1, column=0, columnspan=4, padx=0, pady=0, ipadx=45, ipady=10, sticky=W)

b1 = Button(f1, text="Clear", bg=b_fun, fg=b_fun1, font="arial 14", width=8, height=1, relief="groove", anchor="center", command=lambda: clear())
b2 = Button(f1, text="<-", bg=b_fun, fg=b_fun1, font="arial 14", width=8, height=1, relief="groove", anchor="center", command=lambda: backspace())
b3 = Button(f1, text="%", bg=b_fun, fg=b_fun1, font="arial 14", width=8, height=1, relief="groove", anchor="center", command=lambda: get('%'))
b4 = Button(f1, text="/", bg=b_fun, fg=b_fun1, font="arial 14", width=8, height=1, relief="groove", anchor="center", command=lambda: input('/'))
b5 = Button(f1, text="7", bg=b_num, fg=b_num1, font="arial 14", width=8, relief="groove", anchor="center", command=lambda: input('7'))
b6 = Button(f1, text="8", bg=b_num, fg=b_num1, font="arial 14", width=8, height=1, relief="groove", anchor="center", command=lambda: input('8'))
b7 = Button(f1, text="9", bg=b_num, fg=b_num1, font="arial 14", width=8, height=1, relief="groove", anchor="center", command=lambda: input('9'))
b8 = Button(f1, text="x", bg=b_fun, fg=b_fun1, font="arial 14", width=8, height=1, relief="groove", anchor="center", command=lambda: get('x'))
b9 = Button(f1, text="4", bg=b_num, fg=b_num1, font="arial 14", width=8, height=1, relief="groove", anchor="center", command=lambda: input('4'))
b10 = Button(f1, text="5", bg=b_num, fg=b_num1, font="arial 14", width=8, height=1, relief="groove", anchor="center", command=lambda: input('5'))
b11 = Button(f1, text="6", bg=b_num, fg=b_num1, font="arial 14", width=8, height=1, relief="groove", anchor="center", command=lambda: input('6'))
b12 = Button(f1, text="-", bg=b_fun, fg=b_fun1, font="arial 14", width=8, height=1, relief="groove", anchor="center", command=lambda: get('-'))
b13 = Button(f1, text="1", bg=b_num, fg=b_num1, font="arial 14", width=8, height=1, relief="groove", anchor="center", command=lambda: input('1'))
b14 = Button(f1, text="2", bg=b_num, fg=b_num1, font="arial 14", width=8, height=1, relief="groove", anchor="center", command=lambda: input('2'))
b15 = Button(f1, text="3", bg=b_num, fg=b_num1, font="arial 14", width=8, height=1, relief="groove", anchor="center", command=lambda: input('3'))
b16 = Button(f1, text="+", bg=b_fun, fg=b_fun1, font="arial 14", width=8, height=1, relief="groove", anchor="center", command=lambda: get('+'))
b18 = Button(f1, text="0", bg=b_num, fg=b_num1, font="arial 14", width=8, height=1, relief="groove", anchor="center", command=lambda: input('0'))
b19 = Button(f1, text=".", bg=b_fun, fg=b_fun1, font="arial 14", width=8, height=1, relief="groove", anchor="center",command=lambda: input('.'))
b20 = Button(f1, text="=", bg="orange", fg=b_fun1, font="arial 14", width=17, height=1, relief="groove", anchor="center", command=lambda: calculate())
b1.grid(row=2, column=0, columnspan=1, padx=0, pady=0)
b2.grid(row=2, column=1, columnspan=1, padx=0, pady=0)
b3.grid(row=2, column=2, columnspan=1, padx=0, pady=0)
b4.grid(row=2, column=3, columnspan=1, padx=0, pady=0)
b5.grid(row=3, column=0, columnspan=1, padx=0, pady=0)
b6.grid(row=3, column=1, columnspan=1, padx=0, pady=0)
b7.grid(row=3, column=2, columnspan=1, padx=0, pady=0)
b8.grid(row=3, column=3, columnspan=1, padx=0, pady=0)
b9.grid(row=4, column=0, columnspan=1, padx=0, pady=0)
b10.grid(row=4, column=1, columnspan=1, padx=0, pady=0)
b11.grid(row=4, column=2, columnspan=1, padx=0, pady=0)
b12.grid(row=4, column=3, columnspan=1, padx=0, pady=0)
b13.grid(row=5, column=0, columnspan=1, padx=0, pady=0)
b14.grid(row=5, column=1, columnspan=1, padx=0, pady=0)
b15.grid(row=5, column=2, columnspan=1, padx=0, pady=0)
b16.grid(row=5, column=3, columnspan=1, padx=0, pady=0)
b18.grid(row=6, column=1, columnspan=1, padx=0, pady=0)
b19.grid(row=6, column=0, columnspan=1, padx=0, pady=0)
b20.grid(row=6, column=2, columnspan=2, padx=0, pady=0)

f1.mainloop()
