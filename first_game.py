import os
import time
import sys, tty, termios
from text import *
from game_start import *
from game_inventory import *

WALLS = ['#', '''\'''', '/', '|', '-']

class colours:
    Blue = '\033[94m'
    Green = '\033[92m'
    Yellow = '\033[93m'
    Barier = '\033[0m'
    Bold = '\033[1m'
    Underline = '\033[4m'
    Red = '\033[31m'


class background:
    black = '\033[40m'
    red = '\033[41m'
    green = '\033[42m'
    orange = '\033[43m'
    blue = '\033[44m'
    purple = '\033[45m'
    cyan = '\033[46m'
    lightgrey = '\033[47m'


def main_stage(board):
    file_name = 'stage1.txt'
    row = []
    board = []

    text = open(file_name, "r").readlines()
    for line in text:
        for char in line:
            row.append(char)
        board.append(row)
        row = []
    for line in board:
        line[-1] = line[-1].strip()

    return board


def print_board(board):

    for row in board:
        for char in row:
            if char == '#':
                    print(background.red + colours.Red + char + colours.Barier, end='')
            elif char == '@':
                print(colours.Blue + char, end='')
            elif char.isalpha():
                print(colours.Blue + char, end='')
            elif char == '8':
                print(background.cyan + colours.Yellow + char + colours.Barier, end='')
            else:
                print(colours.Green + char + colours.Barier, end='')
        print(end='\n')
    print(print_table(inventory))


def insert_player(fuel, board, x, y):

    board[y][x] = "@"
    return board


def getch():

    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def fuel_down(fuel):

    fuel -= 2
    print(fuel)


def move_player(fuel, board, x, y):

    pressed_key = getch()
    if pressed_key == 'w' and board[y - 1][x] not in WALLS:
        y -= 1
    elif pressed_key == 's' and board[y + 1][x] not in WALLS:
        y += 1
    elif pressed_key == 'a' and board[y][x - 1] not in WALLS:
        x -= 1
    elif pressed_key == 'd' and board[y][x + 1] not in WALLS:
        x += 1
    elif pressed_key == 'x':
        x = "exit"
        game_end()
    print(fuel_down(fuel))

    return x, y


def welcome():

    print_menu()
    os.system('clear')
    print(welcom)
    skip()
    choose_spaceship()
    skip()


def main():

    x = 5
    y = 5
    fuel = 300
    board = []

    welcome()
    while x != "exit":
        os.system('clear')
        board = main_stage(board)
        '''if board[x][y] == board[8][36]:
              file_name == "maze_board.txt"'''
        board = insert_player(fuel, board, x, y)
        print_board(board)
        x, y = move_player(fuel, board, x, y)
        fuel_down(fuel)


if __name__ == "__main__":
    main()
