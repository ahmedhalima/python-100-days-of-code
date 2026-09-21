from json import JSONDecodeError
from tkinter import messagebox
from tkinter import *
import secrets
import string
import json

#----------------- Search website --------------------#
def search_website():
    website = website_input.get()
    if website == '':
        messagebox.showerror("Error", "Please fill in website field.")
        return

    with open('data.json', 'r') as data_file:
        data = json.load(fp=data_file)

        value = next((v for k, v in data.items() if k.lower() == website.lower()), None)
        if value is not None:
            messagebox.showinfo(f'{website.capitalize()}', f"Email:{value['email']}\nPassword: {value['password']}\n")
        else:
            messagebox.showerror("Error", f"No results for {website}")
#----------------- Search website --------------------#

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
        new_data = {
            website: {
                'email': email,
                'password': password
            }
        }
        try:
            with open('data.json', 'r') as data_file:
                data = json.load(fp=data_file)
        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        except JSONDecodeError:
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open('data.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
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

website_search_btn = Button(text='Search', command=search_website)
website_search_btn.grid(column=3, row=1,)
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