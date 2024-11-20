from datetime import datetime
import os

digits = {
    ":": [
        "    ",
        " :: ",
        "    ",
        " :: ",
        "    "
    ],
    "0": [
        " ## ",
        "#  #",
        "#  #",
        "#  #",
        " ## "
    ],
    "1": [
        "   #",
        "   #",
        "   #",
        "   #",
        "   #",
    ],
    "2": [
        "### ",
        "   #",
        " ## ",
        "#   ",
        "####"
    ],
    "3": [
        "### ",
        "   #",
        " ## ",
        "   #",
        "### "
    ],
    "4": [
        "  # ",
        " #  ",
        "####",
        "  # ",
        " #  ",
    ],
    "5": [
        "####",
        "#   ",
        "### ",
        "   #",
        "### ",
    ],
    "6": [
        "  # ",
        " #  ",
        "### ",
        "#  #",
        " ## ",
    ],
    "7": [
        "####",
        "   #",
        "  # ",
        " #  ",
        "#   ",
    ],
    "8": [
        " ## ",
        "#  #",
        " ## ",
        "#  #",
        " ## ",
    ],
    "9": [
        " ## ",
        "#  #",
        " ###",
        "  # ",
        " #  ",
    ],
}


def get_time():
    prev_time = 0
    while True:
        time = datetime.now().strftime("%H:%M:%S")

        if time != prev_time:
            prev_time = time
            os.system("cls")

            ascii_lines = [""] * 5
            for char in time:
                for i in range(5):
                    ascii_lines[i] += digits[char][i] + " "

            for line in ascii_lines:
                print(line)


if __name__ == "__main__":
    get_time()
