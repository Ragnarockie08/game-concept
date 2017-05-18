import os
from text import *
import time
import sys
from game_inventory import choose_spaceship, skip


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
