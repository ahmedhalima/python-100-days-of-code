from tkinter import *
from tkinter import messagebox
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
data = pd.read_csv('data/french_words.csv')
data_dict = data.to_dict(orient="records")
job_id = None
########## Generate a random word
def next_card(know = True):
    if len(data_dict) > 0:
        current_card = random.choice(data_dict)
        data_dict.remove(current_card)
    else:
        messagebox.showinfo('Success', 'You have successfully completed the progress')
        return
    global job_id
    if job_id is not None:
        window.after_cancel(job_id)
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(title_txt, fill="white", text="French")
    canvas.itemconfig(word_txt, fill="white",text=current_card['French'])
    job_id = window.after(3000, flip_card, current_card)


def flip_card(current_card):
    canvas.itemconfig(canvas_image, image=card_front_img)
    canvas.itemconfig(title_txt, fill="black", text='English')
    canvas.itemconfig(word_txt, fill="black", text=current_card['English'])
########## Generate a random word

# set up the layout
window = Tk()
window.title('Flash Card Game')
window.configure(bg=BACKGROUND_COLOR, pady=50, padx=50)
window.resizable(FALSE, FALSE)

# draw the canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_img)

# add text
title_txt = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word_txt = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))

canvas.grid(row=0, column=0, columnspan=2)

# buttons
unknown_img = PhotoImage(file="images/wrong.png")
unknown_btn = Button(image=unknown_img, highlightthickness=0,
    relief="flat",
    borderwidth=0,
    bg=BACKGROUND_COLOR,
    activebackground=BACKGROUND_COLOR, command=lambda: next_card(FALSE))
unknown_btn.grid(row=1, column=0)

known_img = PhotoImage(file="images/right.png")
known_btn = Button(image=known_img, highlightthickness=0,
    relief="flat",
    borderwidth=0,
    bg=BACKGROUND_COLOR, command=next_card,
    activebackground=BACKGROUND_COLOR)
known_btn.grid(row=1, column=1)

next_card()

window.mainloop()
