import art
from termcolor import colored


def choose_font():
    art.font_list("test", "ascii")
    return input("choose the font to use: ")


def choose_color() -> int:
    return int(input("choose the color to use: \n"
                     "1. Black \n"
                     "2. Red \n"
                     "3. Blue \n"
                     ">> "))


while True:
    color_text = '\033[%dm%s'
    text = input("enter a text for your art: ")
    font = choose_font()
    color = choose_color()

    color_number = 0

    if color == 2:
        color_number = 91
    elif color == 3:
        color_number = 94

    new_art = art.text2art(text, font)
    print(color_text % (color_number, new_art))
