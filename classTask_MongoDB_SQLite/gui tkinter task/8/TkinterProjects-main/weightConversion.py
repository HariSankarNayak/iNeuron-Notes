from tkinter import *

window = Tk()
window.geometry("625x150")
window.title("Weight Converting Tool")


def convert_from_kg():
    grams = round(float(entry_value.get()) * 1000,2)
    pounds = round(float(entry_value.get()) * 2.20462,2)
    ounces = round(float(entry_value.get()) * 35.274,2)

    text1.insert(END, grams)
    text2.insert(END, pounds)
    text3.insert(END, ounces)


label = Label(window, text="Enter Weight in Kg", font="times 18 bold")
label.grid(row=0, column=0)

entry_value = StringVar()
entry = Entry(window, textvariable=entry_value, font=('calibre', 10, 'bold'))
entry.grid(row=0, column=1)

button = Button(window, text="Convert", command=convert_from_kg, font="times 18 bold", borderwidth=10)
button.grid(row=0, column=2)

l1 = Label(window, text="Grams", font="times 18 bold")
l1.grid(row=2, column=0)
l2 = Label(window, text="Pounds", font="times 18 bold")
l2.grid(row=2, column=1)
l3 = Label(window, text="Ounces", font="times 18 bold")
l3.grid(row=2, column=2)

text1 = Text(window, height=2, width=20, font="times 15 bold", bg='orange')
text1.grid(row=1, column=0)

text2 = Text(window, height=2, width=20, font="times 15 bold", bg='white')
text2.grid(row=1, column=1)

text3 = Text(window, height=2, width=20, font="times 15 bold", bg='green')
text3.grid(row=1, column=2)

window.mainloop()