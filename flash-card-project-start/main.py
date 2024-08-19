from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

# Reading the csv file
data = pandas.read_csv('data/french_words.csv')
french_data = data.to_dict(orient='records')
print(french_data)


def flip_card(french_word):
    english_word = current_card['English']
    window.card_back_image = PhotoImage(file='images/card_back.png')
    canvas.itemconfig(canvas_image, image=window.card_back_image)
    canvas.itemconfig(language_name_text, fill='white', text='English')
    canvas.itemconfig(word_text,text=english_word,fill='white')


def is_known():
    global current_card
    french_data.remove(current_card)
    generate_word()


# Creating function for French words
def generate_word():
    random_dictionary = random.choice(french_data)
    global current_card
    current_card = random_dictionary
    random_word = random_dictionary['French']
    window.card_front_image = PhotoImage(file='images/card_front.png')
    canvas.itemconfig(canvas_image, image=window.card_front_image)
    canvas.itemconfig(language_name_text, fill='black', text='French')
    canvas.itemconfig(word_text, text=random_word, fill='black')

    window.after(3000, flip_card, random_word)


# Setting up the windows
window = Tk()
window.title("Flash Card Project.")
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)

canvas = Canvas(width=800, height=530, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file='images/card_front.png')
canvas_image = canvas.create_image(400, 265, image=front_image)
language_name_text = canvas.create_text(400, 150, text='French', font=('Arial', 40, 'italic'))
word_text = canvas.create_text(400, 263, text='word', font=('Arial', 40, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

wrong_button_image = PhotoImage(file='images/wrong.png')
wrong_button = Button(image=wrong_button_image, justify="center", highlightthickness=0, width=100, height=99,
                      command=generate_word)
wrong_button.grid(row=1, column=0)

right_button_image = PhotoImage(file='images/right.png')
right_button = Button(image=right_button_image, justify="center", highlightthickness=0, width=100, height=99,
                      command=is_known)
right_button.grid(row=1, column=1)
window.mainloop()
