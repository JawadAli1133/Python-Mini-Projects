from tkinter import *

window = Tk()
window.title("Miles to Kilometer converter")
window.config(padx=20, pady=20)

entry = Entry(width=5)
entry.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

equal_to_label = Label(text="is equal to")
equal_to_label.grid(row=1, column=0)

result_label = Label(text='0')
result_label.grid(row=1, column=1)

km_label = Label(text='Kilometers')
km_label.grid(row=1, column=2)


def convert_to_kilo_meters():
    entry_input = entry.get()
    result = 0
    if entry_input.isnumeric():
        result = round(float(entry_input) * 1.609, 4)
    result_label['text'] = str(result)


convert_button = Button(text="Convert", command=convert_to_kilo_meters)
convert_button.grid(row=2, column=1)

window.mainloop()



