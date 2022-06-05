#age calculator
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox, Entry
from datetime import date
from datetime import datetime
from dateutil import relativedelta

current_time = datetime.now()
day_c = int(current_time.day)
month_c = int(current_time.month)
year_c = int(current_time.year)

def clear():
    input1_day.delete(0, END)
    input1_month.delete(0, END)
    input1_year.delete(0, END)
    result.delete(0,END)

def age_calc():

    try:
        day_d = int(input1_day.get())
        month_d = int(input1_month.get())
        year_d = int(input1_year.get())

        date1 = datetime(year_c,month_c,day_c)
        date2 = datetime(year_d,month_d,day_d)

        diff = relativedelta.relativedelta(date1, date2)

        years = diff.years
        months = diff.months
        days = diff.days

        age = str(years) + " years," + str(months) +"months," + str(days) + "days"

        result.insert(0,age)
    except:
        messagebox.showinfo("Warning:","Enter valid dates")

root = Tk()
root.geometry("550x350+350+100")
root.title("Age Calculator")

Label(root, text="Age Calculator", font='arial 20 bold').grid(row=0,column=1)

#dummy labels for spacing
Label(root).grid(row=1,column=0)
Label(root,text="              ").grid(row=1,column=0)
Label(root).grid(row=3,column=1)
Label(root).grid(row=5,column=1)
Label(root).grid(row=7,column=1)
Label(root).grid(row=9,column=1)

#input 1 label
input1_label = Label(root,text="Enter your date of birth : ", font="arial 10 bold")
input1_label.grid(row=2,column=1,sticky=W)

#input 1 entry
input1_day = Entry(root)
input1_day.config(width=6)
input1_day.grid(row=2,column=2,sticky=E)
input1_day.insert(0,'Day')

input1_month = Entry(root)
input1_month.config(width=6)
input1_month.grid(row=2,column=3)
input1_month.insert(0,'Month')

input1_year = Entry(root)
input1_year.config(width=6)
input1_year.grid(row=2,column=4)
input1_year.insert(0,'Year')

#input 2 label
input2_label = Label(root, text="Current date :", font="arial 10 bold")
input2_label.grid(row=4,column=1,sticky=W)

#input 2 entry
input2_day = Entry(root)
input2_day.config(width=6)
input2_day.grid(row=4,column=2,sticky=E)
input2_day.insert(0,day_c)

input2_month = Entry(root)
input2_month.config(width=6)
input2_month.grid(row=4,column=3)
input2_month.insert(0,month_c)

input2_year = Entry(root)
input2_year.config(width=6)
input2_year.grid(row=4,column=4)
input2_year.insert(0,year_c)

#calcute button
calc_btn = Button(root,text="Calculate",width=15, command=age_calc)
calc_btn.grid(row=8,column=1, sticky=W)

#clear button
clear_btn = Button(root, text="Clear", width=15, command=clear)
clear_btn.grid(row=8,column=2, sticky=W)

#result label
result_label = Label(root, text="Your current age from DOB :", font="arial 10 bold")
result_label.grid(row=10,column=1, sticky=W)

#result input
result = Entry(root)
result.config(width=25)
result.grid(row=10,column=2,sticky=W)

mainloop()