from tkinter import*
from tkinter import filedialog, messagebox

def showopen():
    file_names = filedialog.askopenfilenames(title="Select file", filetypes=[("All Files","*.*")])
    str =""
    if type(file_names) is tuple:
        for file in file_names:
            str+=file+"\n"
        lbl.configure(text=str,font=10,anchor="nw")
    else:
        messagebox.showinfo("Your selections", "You did not select any file")

f1 =Tk()
f1.title("File explore")
f1.geometry("750x400+350+300")
b1=Button(f1,text="Open file",bg="sky blue",borderwidth=4,width=10,font= "arial 16 bold",relief="raised",command=showopen)
b1.pack()

lbl=Label(f1, bg="white",borderwidth=5,width=60,height=13,font=12,anchor="nw")
lbl.pack()
f1.mainloop()