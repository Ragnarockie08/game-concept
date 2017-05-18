import os
from text import *
import time
import sys
from game_inventory import skip, inventory


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
            print("1: Hints about ships \n2: Choose your ship")
            options = int(input("Choose: "))
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
                inventory['fuel'] = 500
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


def welcome_screen():

    os.system('clear')
    print(welcom)
    skip()
    choose_spaceship()
    skip()


def game_end():

    time.sleep(1)
    os.system('clear')
    print(end)
    time.sleep(2)
    sys.exit()
