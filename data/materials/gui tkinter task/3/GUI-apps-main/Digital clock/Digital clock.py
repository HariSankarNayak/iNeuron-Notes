# Create a digital clock using Tkinter
from tkinter import*
from time import strftime

def clock():
   time = strftime("%H:%M:%S %p")
   l1.config(text=time)
   l1.after(1000, clock)

f1 = Tk()
f1.title("Digital Clock")
f1.geometry("483x114+600+400")
f1.resizable(False,False)

l1 = Label(f1,font=("courier", 50) ,bg="deep sky blue",borderwidth=20, relief="groove",anchor="center")
l1.grid(row=0, column=0, columnspan=1, sticky=E)
clock()

f1.mainloop()
