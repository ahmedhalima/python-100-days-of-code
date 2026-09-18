from tkinter import *

window = Tk()
window.title('Hello')
window.minsize(height=400, width=600)
window.resizable(False, False)

label = Label(text="My Label", font=('Arial', 24))
label.pack()

def change_label():
    label_text = my_input.get()
    label.configure(text=label_text)

my_button = Button(text='Click Me', command=change_label)
my_button.pack()

my_input = Entry()
my_input.pack()

window.mainloop()