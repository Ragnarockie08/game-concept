from speceship import *
import os
from text import *
import time
import sys
import csv
from game_inventory import choose_spaceship, skip
from first_game import getch
from highscore import *


def welcome_screen():

    os.system('clear')
    print(welcom)
    skip()
    choose_spaceship()
    skip()


def game_end():

    os.system('clear')
    # highscore(end_time)
    print(end)
    print("Thanks for playing and see you next time")


    time.sleep(2)
    sys.exit()
