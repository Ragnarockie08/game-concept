from speceship import *
import os
from text import end
import time
import sys

def clear():
    os.system('clear')


def skip():
    skip = input("press S to skip the game or Q to quit")
    os.system('clear')
    if skip.lower() == "q":
        x = "exit"
        game_end()

def game_end():

    os.system('clear')
    print(end)
    print("Thanks for playing and see you next time")
    time.sleep(2)
    sys.exit()


def choose_spaceship():
    spaceships = {"NORMANDIA": "NORMANDIA IS FAST BUT WASTE MORE FUEL THEN THE OTHERS",
                  "HETMAN": "HETMAN IS SLOW BUT HAVE HUGE HOLD AND ARMOR",
                  "PROTECTOR": "IS THE BEST IN THE BATTLEFIELD"
                  }
    while True:
        print(ship)
        for key in spaceships:
            print(key)
        try:
            options = int(input("Press 1 to get hints about ships or 2 to choose your ship for whole game"))
        except ValueError:
            clear()
            continue
        if options == 1:
            try:
                choose = input("Choose spaceship to see what abilities it has: ").upper()
            except ValueError:
                clear()
                continue
                if choose in spaceships.keys():
                    print(spaceships[choose])
                    skip()
                    continue
        elif options == 2:
            ship_take = input("Choose your spaceship: ").upper()

            if ship_take == "NORMANDIA":
                fuel = 300
                attack = 3
                speed = 3
                armor = 7
                break
            elif ship_take == "HETMAN":
                fuel = 500
                attack = 3
                speed = 1
                armor = 10
                break
            elif ship_take == "PROTECTOR":
                fuel = 300
                attack = 5
                speed = 2
                armor = 5
                break
            else:
                clear()
                continue
        else:
            clear()
            continue
    print("="*180)
    print('''  Your Ship: {}
             Fuel: {}
             attack: {}
             speed: {}
             armor: {}'''
             .format(ship_take, fuel, attack, speed, armor))
    print("="*180)
