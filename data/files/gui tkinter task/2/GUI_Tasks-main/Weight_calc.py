from tkinter import *
from tkinter import messagebox,simpledialog
from tkinter.ttk import Combobox

root = Tk()
root.geometry("440x220+350+100")
root.title("GUI Weight conversion")

def clear():
    input1.delete(0,END)
    result.delete(0,END)
    input1.insert(0,'Enter result')
    result.insert(0,'result')
    combobox.current(0)
    input1.focus()

def convert():
    result.delete(0,END)
    try:
        value = float(input1.get())
        opr = combobox.get()

        if opr == 'Select one':
            messagebox.showinfo('Warning:','Select conversion')
        elif opr == 'Metric ton to Kilograms':
            mt = 1000*value
            res = str(mt) + ' kgs'
            result.insert(0,res)
        elif opr == 'Kilogram to Grams':
            kg = 1000*value
            res = str(kg) + ' g'
            result.insert(0,res)
        elif opr == 'Hectograms to Grams':
            hg = 100*value
            res = str(hg) + ' g'
            result.insert(0,res)
        elif opr == 'Dekagrams to Grams':
            dkg = 10*value
            res = str(dkg) + ' g'
            result.insert(0,res)
        elif opr == 'Gram to Decigrams':
            g = 10*value
            res = str(g) + ' dg'
            result.insert(0,res)
        elif opr == 'Decigram to Centigrams':
            dg = 10*value
            res = str(dg) + ' cg'
            result.insert(0,res)
        elif opr == 'Centigrams to Milligrams':
            cg = 10*value
            res = str(cg) + ' mg'
            result.insert(0,res)
    except:
        messagebox.showinfo('Warning:','Enter valid details')

Label(root, text="Weight Conversion", font='arial 20 bold').grid(row=0, column=1)

#dummy label for spacing
Label(root, width=10).grid(row=0,column=0)

#input 1
input1 = Entry(root)
input1.config(width=15)
input1.place(x=40,y=60)
input1.insert(0,'Enter value')

#combo box
options =['Select one','Metric ton to Kilograms','Kilogram to Grams','Hectograms to Grams','Dekagrams to Grams','Gram to Decigrams','Decigram to Centigrams','Centigrams to Milligrams']
combobox = Combobox(root,values=options)
combobox.config(width=20)
combobox.place(x=145,y=60)
combobox.current(0)

#result input
result = Entry(root)
result.config(width=15)
result.place(x=300,y=60)
result.insert(0,'result')

#conversion button
btn = Button(root,text='Convert',width=15,command=convert)
btn.place(x=70,y=110)

#clear button
btn_clr = Button(root,text='Clear',width=15,command=clear)
btn_clr.place(x=250,y=110)

mainloop()