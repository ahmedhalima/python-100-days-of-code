from tkinter import *
from tkinter import messagebox

def mile_to_km():
    try:
        miles = float(miles_input.get())
        km = round(miles * 1.609)
        kilometer_result_label.config(text=f"{km}")
    except ValueError:
        print('error')
        messagebox.showinfo('Error', 'Please enter and integer value')

window = Tk()
window.title = 'mile to KM converter'
window.configure(padx=20, pady=20)
window.resizable(FALSE, FALSE)

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text='Miles')
miles_label.grid(column=2, row=0)

is_equal_label = Label(text='is equal to')
is_equal_label.grid(column=0, row=1)

kilometer_result_label = Label(text='0')
kilometer_result_label.grid(column=1, row=1)

kilometer_label = Label(text='KM')
kilometer_label.grid(column=2, row=1)

calculate_btn = Button(text='Calculate', command=mile_to_km)
calculate_btn.grid(column=1, row=2)



window.mainloop()