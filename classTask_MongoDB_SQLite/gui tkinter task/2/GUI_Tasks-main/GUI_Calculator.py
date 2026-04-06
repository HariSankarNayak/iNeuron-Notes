# gui calculator
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox


def operation():
    try:
        result.delete(0, END)

        num1 = float(input1.get())
        num2 = float(input2.get())
        opr = combobox.get()

        if opr == 'Select one':
            messagebox.showinfo("Warning:", "Select any one operator")
        elif opr == 'Addition':
            res = num1 + num2
            result.insert(0, res)
        elif opr == 'Subtraction':
            res = num1 - num2
            result.insert(0, res)
        elif opr == 'Multiplication':
            res = num1 * num2
            result.insert(0, res)
        elif opr == 'Divison':
            res = num1 / num2
            result.insert(0, res)

    except:
        messagebox.showinfo("Warning:", "Enter valid numbers only")


def clear():
    input1.delete(0, END)
    input2.delete(0, END)
    result.delete(0, END)
    combobox.current(0)


root = Tk()
root.geometry("400x350+350+100")
root.title("GUI Calculator")

Label(root, text="Calculator", font='arial 20 bold').grid(row=0, column=1)

# dummy labels for spacing
Label(root).grid(row=1, column=0)
Label(root, text="              ").grid(row=1, column=0)
Label(root).grid(row=3, column=1)
Label(root).grid(row=5, column=1)
Label(root).grid(row=7, column=1)
Label(root).grid(row=9, column=1)

# input 1 label
input1_label = Label(root, text="Enter first number: ", font="arial 10 bold")
input1_label.grid(row=2, column=1, sticky=W)

# input 1 entry
input1 = Entry(root)
input1.grid(row=2, column=2)

# input 2 label
input2_label = Label(root, text="Enter second number:", font="arial 10 bold")
input2_label.grid(row=4, column=1, sticky=W)

# input 2 entry
input2 = Entry(root)
input2.grid(row=4, column=2)

# dropdown
options = ['Select one', 'Addition', 'Subtraction', 'Multiplication', 'Divison']
combobox = Combobox(root, values=options)
combobox.grid(row=6, column=1)
combobox.current(0)

# calcute button
calc_btn = Button(root, text="Calculate", width=15, command=operation)
calc_btn.grid(row=8, column=1)

# clear button
clear_btn = Button(root, text="Clear", width=15, command=clear)
clear_btn.grid(row=8, column=2)

# result label
result_label = Label(root, text="Your result :", font="arial 10 bold")
result_label.grid(row=10, column=1)

# result input
result = Entry(root)
result.grid(row=10, column=2, sticky=E)

mainloop()