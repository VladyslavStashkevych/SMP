import art


def choose_font():
    art.font_list("test", "ascii")
    return input("Choose the font to use: ")


def choose_color() -> int:
    return int(input("Choose the color to use: \n"
                     "1. Black \n"
                     "2. Red \n"
                     "3. Blue \n"
                     ">> "))


def choose_width() -> int:
    return int(input("Enter width as a number of spaces: "))


def get_art(font_name: str = "z-pilot", color_choice: int = 0, spaces: int = 0) -> str:
    color_text = '\033[%dm%s\033[0m'
    text = input("Enter a text for your art: ")

    color_number = 0

    if color_choice == 2:
        color_number = 91
    elif color_choice == 3:
        color_number = 94

    new_art = art.text2art(text, font_name, space = spaces)
    return color_text % (color_number, new_art)


def write_into_file(file_path, content):
    with open(file_path, "a") as file:
        file.write(content)


def read_from_file(file_path):
    with open(file_path, "r") as file:
        return file.read()


font = "z-pilot"
color = 0
width = 0

while True:
    choice = int(input("Choose one: \n"
                       "1. Make an art\n"
                       "2. Change art font\n"
                       "3. Change art color\n"
                       "4. Change art width\n"
                       "5. See previous arts\n"
                       "6. Exit\n"
                       ">> "))

    if choice == 1:
        art_text = get_art(font, color, width)
        print(art_text)
        choice = int(input("Choose the next action: \n"
                           "1. Save an art\n"
                           "2. Return to the main menu\n"
                           "3. Exit\n"
                           ">> "))
        if choice == 1:
            write_into_file("art.txt", art_text)
        elif choice == 3:
            break

    elif choice == 2:
        font = choose_font()
    elif choice == 3:
        color = choose_color()
    elif choice == 4:
        width = choose_width()
    elif choice == 5:
        print(read_from_file("art.txt"))
    elif choice == 6:
        break
    else:
        print("Wrong choice, try again :(")
