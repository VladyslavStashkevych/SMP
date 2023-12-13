def choose_symbol() -> str:
    try:
        ch = input("Symbols: *, #, @\n"
                   "Choose the symbol to use for art: ")
        if ch != "#" and ch != "@" and ch != "*":
            raise ValueError()
    except ValueError:
        print("Wrong choice, try again")
        return choose_symbol()


def choose_color() -> int:
    try:
        return int(input("Choose the color to use: \n"
                         "1 - White \n"
                         "2 - Red \n"
                         "3 - Blue \n"
                         ">> "))
    except ValueError:
        print("Wrong choice, try again")
        return choose_color()


def choose_width() -> int:
    try:
        return int(input("Enter width as a number of spaces: "))
    except ValueError:
        print("Wrong choice, try again")
        return choose_width()


def choose_height() -> int:
    try:
        return int(input("Enter width as a number of enters: "))
    except ValueError:
        print("Wrong choice, try again")
        return choose_height()


def choose_alignment() -> int:
    try:
        return int(input("0 - default\n"
                         "1 - center\n"
                         "2 - right\n"
                         "Where the art should be: "))
    except ValueError:
        print("Wrong choice, try again")
        return choose_alignment()


def get_art(art_symbol: str = "#", color_choice: int = 0, spaces: int = 0, enters: int = 0, align: int = 0) -> str:
    color_text = '\033[%dm%s\033[0m'
    text = input("Enter a text for your art: ")

    color_number = 0

    if color_choice == 2:
        color_number = 91
    elif color_choice == 3:
        color_number = 94

    new_art = make_art(text, art_symbol, spaces, enters, align)
    return color_text % (color_number, new_art)


def make_art(text: str = "test", art_symbol: str = "#", spaces: int = 0, enters: int = 0, align: int = 0):
    text = text.upper()
    formatted_text = ""

    if align == 1:
        formatted_text = "   "
    elif align == 2:
        formatted_text = "      "

    for ch in text:
        formatted_text += ch
        for i in range(spaces):
            formatted_text += " "

    ascii_letters = {
        'A': ["   *   ", "  * *  ", " *   * ", " *** ", " *   * ", " *   * ", " *   * "],
        'B': [" **   ", " *  *  ", " *   * ", " **   ", " *  *  ", " *   * ", " **   "],
        'C': ["  **  ", " *   * ", " *      ", " *      ", " *      ", " *   * ", "  **  "],
        'D': [" **   ", " *  *  ", " *   * ", " *   * ", " *   * ", " *  *  ", " **   "],
        'E': [" *** ", " *      ", " *      ", " *** ", " *      ", " *      ", " *** "],
        'F': [" *** ", " *      ", " *      ", " **   ", " *      ", " *      ", " *      "],
        'G': ["  **  ", " *   * ", " *      ", " *  *  ", " *   * ", " *   * ", "  **  "],
        'H': [" *   * ", " *   * ", " *   * ", " *** ", " *   * ", " *   * ", " *   * "],
        'I': [" *** ", "   *   ", "   *   ", "   *   ", "   *   ", "   *   ", " *** "],
        'J': [" *** ", "    *  ", "    *  ", "    *  ", "    *  ", " *  * ", "  ** "],
        'K': [" *   * ", " *  *  ", " * *   ", " **    ", " * *   ", " *  *  ", " *   * "],
        'L': [" *      ", " *      ", " *      ", " *      ", " *      ", " *      ", " *** "],
        'M': [" *     *     *", " *   **   *", " *  * *  * ", " * *   * * ", " **     ** ", " *       *   ", " *       *   "],
        'N': [" *   * ", " *  ** ", " * * * ", " *   *  ", " *    * ", " *    * ", " *    * "],
        'O': ["  **  ", " *   * ", " *   * ", " *   * ", " *   * ", " *   * ", "  **  "],
        'P': [" **   ", " *  *  ", " *   * ", " **   ", " *      ", " *      ", " *      "],
        'Q': ["  **  ", " *   * ", " *   * ", " *   * ", " * ** ", " *  ** ", "  *** "],
        'R': [" **   ", " *  *  ", " *   * ", " **   ", " * *   ", " *  *  ", " *   * "],
        'S': ["  **  ", " *      ", " *      ", "  **  ", "     * ", " *   * ", "  **  "],
        'T': [" *** ", "   *   ", "   *   ", "   *   ", "   *   ", "   *   ", "   *   "],
        'U': [" *   * ", " *   * ", " *   * ", " *   * ", " *   * ", " *   * ", "  *** "],
        'V': [" *    * ", " *    * ", " *    * ", "  *  *  ", "  *  *  ", "   **   ", "    *    "],
        'W': [" *    *    *", " *   **   *", " *  * *  * ", " * *   * * ", " **     ** ", " *       *   ", " *       *   "],
        'X': [" *   * ", "  * *  ", "   **   ", "    *    ", "   **   ", "  * *  ", " *   * "],
        'Y': [" *   * ", "  * *  ", "   **   ", "    *    ", "    *    ", "    *    ", "    *    "],
        'Z': [" *** ", "    *  ", "   *   ", "  *    ", " *     ", " *     ", " *** "],
        ' ': [" ", " ", " ", " ", " ", " ", " "],
    }

    end_text = ""

    for line in range(7):
        for ch in formatted_text:
            if ch in ascii_letters:
                max_line_length = max(len(line) for line in ascii_letters.get(ch, ['']))
                current_line = ascii_letters[ch][line]
                padded_line = f"{current_line:<{max_line_length}}"
                end_text += padded_line.replace('*', symbol)
        for i in range(enters + 1):
            end_text += "\n"

    return end_text


def write_into_file(file_path, content):
    with open(file_path, "a") as file:
        file.write(content)


def read_from_file(file_path):
    with open(file_path, "r") as file:
        return file.read()


symbol = "#"
color = 0
width = 0
height = 0
alignment = 0

while True:
    try:
        choice = int(input("Choose one: \n"
                           "1 - Make an art\n"
                           "2 - Change art symbol\n"
                           "3 - Change art color\n"
                           "4 - Change art width\n"
                           "5 - Change art height\n"
                           "6 - Change art alignment\n"
                           "7 - See previous arts\n"
                           "8 - Exit\n"
                           ">> "))

        if choice == 1:
            art_text = get_art(symbol, color, width, height, alignment)
            print(art_text)
            choice = int(input("Choose the next action: \n"
                               "1 - Save an art\n"
                               "2 - Return to the main menu\n"
                               "3 - Exit\n"
                               ">> "))
            if choice == 1:
                write_into_file("art.txt", art_text)
            elif choice == 3:
                break

        elif choice == 2:
            font = choose_symbol()
        elif choice == 3:
            color = choose_color()
        elif choice == 4:
            width = choose_width()
        elif choice == 5:
            height = choose_height()
        elif choice == 6:
            alignment = choose_alignment()
        elif choice == 7:
            print(read_from_file("art.txt"))
        elif choice == 8:
            break
        else:
            print("Wrong choice, try again :(")
    except ValueError:
        print("Wrong choice, try again")
