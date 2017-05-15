from speceship import *
import os
from text import end
import time
import sys
import csv

def clear():
    os.system('clear')


def skip():
    skip = input("press S to move further or Q to quit")
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
    spaceships = {"1.NORMANDIA": "NORMANDIA IS FAST BUT WASTE MORE FUEL THEN THE OTHERS",
                  "2.PROTECTOR": "IS THE BEST IN THE BATTLEFIELD"
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
                fuel = 500
                attack = 3
                speed = 3
                armor = 7
                break
            elif ship_take == "2":
                fuel = 500
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
    print('''
             Fuel: {}
             attack: {}
             speed: {}
             armor: {}'''
             .format(fuel, attack, speed, armor))
    print("="*180)
