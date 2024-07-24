from tkinter import *
import pandas
import csv
import random
BACKGROUND_COLOR = "#B1DDC6"
rw_french = ""
rw_english = ""
timer = ""


# Tick Function
def next_card():
    global rw_french, rw_english, timer
    window.after_cancel(timer)
    random_word = random.choice(dictionary)
    for key,value in random_word.items():
        rw_french = key
        rw_english = value
    canvas.itemconfig(canvas_image, image=card_front_img)
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(word, text= rw_french, fill="black")
    timer = window.after(3000, display_english)


def display_english():
    global rw_english
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=rw_english, fill="white")
    canvas.itemconfig(canvas_image, image=card_back_img)


# Background Window set up
window = Tk()
window["bg"] = BACKGROUND_COLOR
window.config(padx=50, pady=50)
window.title("Flash Card Application")

timer = window.after(3000, display_english)

# Setting Up Canvas
canvas = Canvas()
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
canvas["highlightthickness"] = 0
canvas["width"] = 800
canvas["height"] = 526
canvas["bg"] = BACKGROUND_COLOR
canvas_image = canvas.create_image(400, 263, image=card_front_img)
language = canvas.create_text(400, 150, text="", font=('Ariel', 40, 'italic'))
word = canvas.create_text(400, 263, text="", font=('Ariel', 60, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
tick_button = Button()
tick_image = PhotoImage(file="./images/right.png")
tick_button["image"] = tick_image
tick_button["command"] = next_card
tick_button.grid(row=1, column=1)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image)
wrong_button["command"] = next_card
wrong_button.grid(row=1, column=0)

# CSV File and Pandas
data = pandas.read_csv("./data/french_words.csv")
dictionary = [{data.iloc[i]["French"] : data.iloc[i]["English"]} for i in range(len(data))]

# Causes the programme to start of with a French word
next_card()
window.mainloop()

