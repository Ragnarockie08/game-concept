import csv
from game_start import *

inventory = {'Platyna': 0, 'Pallad': 0, 'Iryd': 0, 'Weapons': 0, 'fuel': 0, 'Armor': 0}

def choose_spaceship():
    spaceships = {"NORMANDIA": "NORMANDIA IS FAST BUT WASTE MORE FUEL THEN THE OTHERS",
                  "PROTECTOR": "IS THE BEST IN THE BATTLEFIELD"
                  }

    while True:
        print(ship)
        print("1.NORMANDIA")
        print("2.PROTECTOR")
        print("="* 30)

        try:
            options = int(input("1: Hints about ships \n2: Choose your ship"))
        except ValueError:
            clear()
            continue
        if options == 1:
            try:
                print("="*30)
                choose = input("Choose spaceship to see what abilities it has: ").upper()
            except ValueError:
                clear()
                continue
            if choose in spaceships.keys():
                print(spaceships[choose])
                skip()
                continue
        elif options == 2:
            print("="*30)
            ship_take = input("Choose your spaceship: (press 1 or 2)").upper()

            if ship_take == "1":
                inventory['fuel'] = 500
                inventory['armor'] = 7
                break
            elif ship_take == "2":
                inventory['fuel'] = 300
                inventory['armor'] = 10
                break
            else:
                clear()
                continue
        else:
            clear()
            continue
    print("="*180)
    print('''
             Fuel: {}
             armor: {}'''
             .format(inventory['fuel'], inventory['armor']))
    print("="*180)


def skip():
    skip = input("press S to move further or Q to quit")
    os.system('clear')
    if skip.lower() == "q":
        x = "exit"
        game_end()


def add_to_inventory(inventory, added_items):
    '''Function that add items form diffrent loots'''

    for item in added_items:
        if item in inventory.keys():
            inventory[item] += 1
        else:
            inventory.update({item: 1})
    return inventory


def print_table(inventory, order='count,desc'):
    '''Function that prints table in diffrent order depending on input'''

    inventory['fuel'] -= 1
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
        print("Total number of items: {}\n".format(sum(inventory.values())))
