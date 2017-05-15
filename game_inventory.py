import csv
from game_start import *


inventory = {'Platyna': 0, 'Pallad': 0, 'Iryd': 0, 'Weapons': 1, 'fuel': 500}
loot = ['Platyna', 'Pallad', 'Iryd', 'Fuel']


def display_inventory(inventory):
    '''Function that prints invetory'''
    print("\nYour inventory:\n")
    for key, value in inventory.items():
        print(key, value)
    print("Total number of items: {}\n".format(sum(inventory.values())))


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


def import_inventory(inventory, filename="import_inventory.csv"):
    '''Functions reads inventory from csv file'''

    with open(filename, 'r') as infile:
        for line in infile:
            loot_list = (line.strip().split(','))
    player_items = add_to_inventory(inventory, loot_list)
    return player_items


def export_inventory(inventory, filename="export_inventory.csv"):
    '''Function write inventory to csv file'''

    with open(filename, 'w') as outfile:
        writer = csv.writer(outfile)
        list_items = []
        for key, value in inventory.items():
            for numbers in range(value):
                list_items.append(key)
        list_items = ",".join(list_items)
        outfile.write(list_items)




'''display_inventory(inventory)
player_items = add_to_inventory(inventory, enemy_loot)
print_table(player_items, "count,desc")
player_items = import_inventory(inventory, filename="import_inventory.csv")
print_table(player_items, "count,asc")
export_inventory(player_items, filename="export_inventory.csv")'''
