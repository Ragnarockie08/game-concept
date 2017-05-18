import os
import csv
from game_start import *
from game_menu import getch

inventory = {'Platinum': 0, 'Palladium': 0, 'Iridium': 0, 'Weapons': 0, 'fuel': 300, 'Armor': 5, 'Level': 1, 'Key': 0}

def choose_spaceship():
    spaceships = {"NORMANDIA": "NORMANDIA HAVE HUGE TANK",
                  "PROTECTOR": "PROTECTOR HAVE UNBROKEN ARMOR"
                  }

    while True:
        print(ship)
        print("1.NORMANDIA")
        print("2.PROTECTOR")
        print("="* 30)

        try:
            options = int(input("1: Hints about ships \n2: Choose your ship"))
        except ValueError:
            os.system('clear')
            continue

        if options == 1:
            print(spaceships['NORMANDIA'])
            print(spaceships['PROTECTOR'])
            skip()
            continue

        elif options == 2:
            print("="*30)
            ship_take = input("Choose your spaceship: (press 1 or 2): ").upper()
            if ship_take == "1":
                inventory['fuel'] = 700
                inventory['Armor'] = 7
                break
            elif ship_take == "2":
                inventory['fuel'] = 400
                inventory['Armor'] = 10
                break
        else:
            os.system('clear')
            continue
    print("="*180)
    print('''
             Fuel: {}
             Armor: {}'''
             .format(inventory['fuel'], inventory['Armor']))
    print("="*180)


def skip():
    print("press S to move further or Q to quit")
    skip = getch().lower()
    os.system('clear')
    if skip == "q":
        x = "exit"
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
