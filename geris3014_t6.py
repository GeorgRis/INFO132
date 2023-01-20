#opg 1
from tkinter import Tk, Label, Button
root = Tk()
count = 0

tekst = Label(root, text=count)
tekst.grid(row=0, column=2)

def pluss():
    global count
    count+=1
    tekst = Label(root, text=count)
    tekst.grid(row=0, column=2)


button = Button(root,
    text='+1',
    width=10,
    height=5,
    command=pluss)
button.grid(row=1, column=2)
root.mainloop()