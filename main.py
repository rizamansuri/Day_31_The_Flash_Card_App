# In the name of Allah, the most Beneficent, the most Merciful...
from tkinter import *
import pandas as pd
import random
import time

BACKGROUND_COLOR = "#B1DDC6"

# Reading the CSV file
all_words_data = pd.read_csv("data/arabic_words.csv")
try:
    not_learned = pd.read_csv("data/words_to_learn.csv")
    is_known = not_learned.to_dict(orient="records")
except FileNotFoundError:
    is_known = all_words_data.to_dict(orient="records")

current_card = {}


# data_dict = {value.Arabic: value.English for (key, value) in data.iterrows()}
# ___________________GENERATE WORDS LEARNED CSV___________________
def learned_words():
    is_known.remove(current_card)
    # print(len(is_known))
    data = pd.DataFrame(is_known)
    data.to_csv("data/words_to_learn.csv", index=False)
    new_card()


# ___________________GENERATE NEW RANDOM CARD___________________
def new_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    # arabic_word, english_word = random.choice(list(data_dict.items()))
    current_card = random.choice(is_known)

    canvas.itemconfig(image_container, image=arabic_txt_image)
    canvas.itemconfig(title, text="Arabic", fill="black")
    canvas.itemconfig(translation, text=current_card["Arabic"], fill="black")
    # To display translation after 3 seconds
    flip_timer = window.after(3000, flip_card)


# ___________________GENERATE TRANSLATION CARD___________________
def flip_card():
    canvas.itemconfig(image_container, image=english_translation_image)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(translation, text=current_card["English"], fill="white")


# Window
window = Tk()
window.title("Riza's Flash Card Game")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)
# Canvas
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
arabic_txt_image = PhotoImage(file="./images/card_front.png")
english_translation_image = PhotoImage(file="./images/card_back.png")
image_container = canvas.create_image(400, 263, image=arabic_txt_image)
title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
translation = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Wrong button
wrong_btn_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_btn_image, highlightthickness=0, command=new_card)
wrong_button.grid(row=1, column=0)

# Right button
right_btn_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_btn_image, highlightthickness=0, command=learned_words)
right_button.grid(row=1, column=1)

new_card()
window.mainloop()
