import time

import characters as chars
from entity import Character
from game import Game


def wait():
    time.sleep(0)


def pick_character():
    lines = [f"#{c['id']} - {c['name']} - {c['desc']}" for c in chars.all]
    print("\n".join(lines))

    choice = input("\n")

    if choice not in [c["name"] for c in chars.all]:
        print("Invalid character, please choose a name from the list.\n")
        pick_character()
    else:
        for char in chars.all:
            if char["name"] == choice:
                return Character(**char)


def main():
    print(("-------------------------------------\n"
           "|                                   |\n"
           "|         Welcome to Aesir!         |\n"
           "|                                   |\n"
           "-------------------------------------\n"))
    wait()

    name = input("Let's begin, firstly, what is your name?\n")
    print(f"Great, so your name is {name}.\n")
    wait()

    print("Before you can begin playing, you must chose a character.")
    print("Please select one of the relevant characters from below.\n")

    character = pick_character()

    game = Game(char=character)
    game.start()


if __name__ == "__main__":
    main()
