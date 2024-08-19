from tkinter import *

window = Tk()

window.title("First Tkinter Project")
window.minsize(width=1000, height=700)

label = Label(text="New Text",font=('Time New Roman', 20, 'bold'))
label.grid(column=0, row=0)

button = Button(text="Click Me")
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

entry = Entry()
entry.grid(column=3, row=2)

window.mainloop()