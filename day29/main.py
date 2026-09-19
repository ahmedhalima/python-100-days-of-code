from tkinter import messagebox
from tkinter import *
import secrets
import string

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = "".join(secrets.choice(alphabet) for _ in range(16))
    password_input.delete(0, END)
    password_input.insert(END, password)
    window.clipboard_clear()
    window.clipboard_append(password)
    window.update()
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_form():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    if website == '' or email == '' or  password == '':
        messagebox.showerror("Error", "Please fill in all fields.")
    else:
        text_to_be_saved = f"{website} | {email} | {password} \n"
        with open('data.txt', 'a') as file:
            file.write(text_to_be_saved)
        website_input.delete(0, END)
        # email_input.delete(0, END)
        password_input.delete(0, END)
        messagebox.showinfo('Success', 'Password Saved Successfully.')
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('password Manager')
window.configure(padx=50, pady=50)
window.minsize(width=500, height=300)
window.resizable(FALSE, FALSE)

canvas = Canvas(width=300, height=200)
image = PhotoImage(file='logo.png')
canvas.create_image(100,100, image=image)
canvas.grid(column=1, row=0, columnspan=2)


# website section
website_label = Label(text='Website:', font=('Arial', 16))
website_label.grid(column=0, row=1)

website_input = Entry(width=35,)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()
# website section

# Email/Username section
email_label = Label(text='Email/Username:', font=('Arial', 16))
email_label.grid(column=0, row=2)

email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(END, 'phpcodertop@gmail.com')
# Email/Username section

# Password section
password_label = Label(text='Password:', font=('Arial', 16))
password_label.grid(column=0, row=3)

password_input = Entry(width=21)
password_input.grid(column=1, row=3,)

password_generate_btn = Button(text='Generate Password', command=generate_password)
password_generate_btn.grid(column=2, row=3,)
# Password section

# Add section
add_btn = Button(text='Add', width=36, command=save_form)
add_btn.grid(column=1, row=4, columnspan=2)
# Add section


window.mainloop()