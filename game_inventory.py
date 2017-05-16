import csv
from game_start import *


inventory = {'Platyna': 0, 'Pallad': 0, 'Iryd': 0, 'Weapons': 0, 'fuel': 200}
loot = ['Platyna', 'Pallad', 'Iryd', 'Fuel']

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
