import tkinter as Tk
from tkinter import filedialog,messagebox
import sys


def browse_file():
    fname = filedialog.askopenfilename(filetypes=(("Template files", "*.type"), ("All files", "*")))
    # print(fname)

    messagebox.showinfo(title='Selected File', message=fname)


root = Tk.Tk()
root.geometry("400x200")
root.configure(bg='yellow')
root.wm_title("Browser")
broButton = Tk.Button(master=root, text='Browse', width=6, command=browse_file, font="times 24 bold", bg="pink")
broButton.pack(side=Tk.LEFT, padx=2, pady=2)

Tk.mainloop()