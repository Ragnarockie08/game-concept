from speceship import *
import os
from text import *
import time
import sys
import csv
from game_inventory import choose_spaceship, skip


def clear():
    os.system('clear')



def welcome_screen():

    os.system('clear')
    print(welcom)
    skip()
    choose_spaceship()
    skip()


def game_end():

    os.system('clear')
    print(end)
    print("Thanks for playing and see you next time")
    time.sleep(2)
    sys.exit()
