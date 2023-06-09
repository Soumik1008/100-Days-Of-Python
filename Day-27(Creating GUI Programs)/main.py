from tkinter import *

window = Tk()
mylabel = Label()
def button_click():
    mylabel.config(text=input.get())


button = Button(text="Click Me", command=button_click)
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

input = Entry(width=20)
input.grid(column=3, row=2)

window.mainloop()