import os
from game_start import *
from read_key import getch

inventory = {'Platinum': 0, 'Palladium': 0, 'Iridium': 0, 'Weapons': 1, 'fuel': 0, 'Armor': 0, 'Level': 1, 'Key': 0}


def skip():
    print("press S to move further or Q to quit")
    skip = getch().lower()
    os.system('clear')
    if skip == "q":
        game_end()


def print_table(inventory, order='count,desc'):
    '''Function that prints table in diffrent order depending on input'''

    print("Inventory: ")
    words = []
    for key in inventory.keys():
        words.append(len(key))
    longest_word = max(words)
    print("Count {} item name".format(" " * longest_word))
    print("----------------{}".format("-" * longest_word))

    if order == 'count,desc':
        sorted_descending_values = sorted(inventory, key=inventory.get, reverse=True)
        for key in sorted_descending_values:
            if inventory[key] > 99:
                print(inventory[key], key.rjust(12+(longest_word)))
            else:
                print(inventory[key], key.rjust(14+(longest_word)))
        print("----------------{}".format("-" * longest_word))
