from tkinter import *
from tkinter import filedialog, messagebox
import os

root = Tk()
root.geometry("410x350+350+100")
root.title("File explorer")

def select_file():
    try:
        input1.delete(0,END)
        file_name = filedialog.askopenfilenames(title="Select file to open", filetypes=[("files", "*.*")])
        input1.insert(0,file_name)
    except:
        messagebox.showinfo('Warning:','Select file to open')

def open_file():
    try:
        file_path = input1.get()
        os.startfile(file_path,'open')
    except:
        messagebox.showinfo('Warning','Select file to open')

#dummy labels for spacing
Label(root, width=5).grid(row=0,column=0)
Label(root, height=1).grid(row=1,column=0)
Label(root, height=1).grid(row=3,column=0)

Label(root, text='File explorer', font='arial 20 bold').grid(row=0,column=1)

#input
input1 = Entry(root)
input1.config(width=50)
input1.grid(row=2,column=1)

#button
btn = Button(root, text='...',command=select_file)
btn.config(height=1,width=3)
btn.grid(row=2,column=2,sticky=E)

#open button
open_btn = Button(root, text='Open selected file',command=open_file)
open_btn.grid(row=4,column=1)




mainloop()
