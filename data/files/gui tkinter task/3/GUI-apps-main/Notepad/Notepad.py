from tkinter import*
from tkinter import filedialog, messagebox

def save_file():
    open_file=filedialog.asksaveasfile(mode="w", defaultextension=".txt")
    if open_file is None:
        return
    text = str(t1.get(1.0,END))
    open_file.write(text)
    open_file.close()

def open_file():
    file = filedialog.askopenfile(mode="r",filetypes=[('text files','*.txt')])
    if file is not None:
        content = file.read()
    t1.insert(INSERT,content)

def clear():
    t1.delete(1.0,END )

def exit():
    result = messagebox.askquestion("Exit", "Are You Sure You Want to Exit?")
    if result == "yes":
        f1.destroy()
    else:
        return None

f1 =Tk()
f1.title("Notepad")
f1.geometry("670x520+350+300")
b1=Button(f1,text="Save file",bg="sky blue",borderwidth=2,width=10,font= "arial 16 bold",relief="raised",command=save_file)
b2=Button(f1,text="Open file",bg="sky blue",borderwidth=2,width=10,font= "arial 16 bold",relief="raised",command=open_file)
b1.grid(row=1, column=0, columnspan=1, padx=0, pady=0)
b2.grid(row=1, column=1, columnspan=1, padx=0, pady=0)

b3=Button(f1,text="Clear",font= "arial 12 ",borderwidth=2,width=10,relief="raised",command=clear)
b4=Button(f1,text="Exit",font= "arial 12 ",borderwidth=2,width=10,relief="raised",command=exit)
b3.grid(row=3, column=0, columnspan=1, padx=0, pady=0)
b4.grid(row=3, column=1, columnspan=1, padx=0, pady=0)

t1=Text(f1, bg="white",height=18,width=55,font=12,wrap=WORD)
t1.grid(row=2, column=0, columnspan=3, padx=0, pady=0)


f1.mainloop()