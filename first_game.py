import os
from time import time, strftime
import sys, tty, termios
from text import *
from game_start import *
from game_inventory import *
from game_menu import *


WALLS = ['#', '''\'''', '/', '|', '-']

class colours:
    Blue = '\033[94m'
    Green = '\033[92m'
    Yellow = '\033[93m'
    Barier = '\033[0m'
    Bold = '\033[1m'
    Underline = '\033[4m'
    Red = '\033[31m'
    Purple = '\033[45m'


class background:
    black = '\033[40m'
    red = '\033[41m'
    green = '\033[42m'
    orange = '\033[43m'
    blue = '\033[44m'
    purple = '\033[45m'
    cyan = '\033[46m'
    lightgrey = '\033[47m'


def create_board(board, filename='stage1.txt'):

    with open(filename, 'r') as f:
        content = f.readlines()
        content = [x.strip() for x in content]
        board = []
        char = ''
        for line in content:
            board.append(list(line))
        return board



def print_board(board):

    for row in board:
        for char in row:
            if char == '#':
                    print(background.red + colours.Red + char + colours.Barier, end='')
            elif char == '@':
                print(colours.Blue + char, end='')
            elif char == '8':
                print(background.cyan + colours.Yellow + char + colours.Barier, end='')
            elif char == '*':
                print(colours.Purple + '⛰️', end='')
            else:
                print(colours.Green + char + colours.Barier, end='')
        print(end='\n')
    print(print_table(inventory))



def insert_player(board, x, y):

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


def highscore(start_time, end_time):
    username = input("Enter yout username!")
    time = str(int(end_time) - int(start_time))
    date = strftime("%d.%m.%Y %H:%M")

    highscore = username + date + time
    return highscore

def collect_elements(board, x, y, inventory):

    if board[y][x] == '*':
        inventory['Platyna'] += 10

    elif board[y][x] == '&':
        inventory['Pallad'] += 10
    elif board[y][x] == '+':
        inventory['Iryd'] += 10
    elif board[y][x] == '%':
        inventory['fuel'] += 50


def move_player(board, x, y):

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
    return x, y

def main():

    x = 5
    y = 5
    board = []
    level = 1

    #print_menu()
    #welcome()
    start_time = time.time()
    while x != 'exit':
        if level == 1:
            board = create_board(board, 'stage1.txt')
        collect_elements(board, x, y, inventory)
        if inventory['fuel'] < 1:
             break
             game_end()
        elif board[y][x] == '8' or level == 2:
            level = 2
            board = create_board(board, 'maze_board.txt')
        elif board[y][x] == '9' or level == 3:
            level = 3
            board = create_board(board, 'maze_board2.txt')
        elif board[y][x] == '7' or level == 4:
            level = 4
            board = create_board(board, 'maze_board2.txt')
        elif board[y][x] == '0':
            level = 1
            board = create_board(board, 'stage1.txt')
        os.system('clear')
        board = insert_player(board, x, y)
        print_board(board)
        x, y = move_player(board, x, y)
    end_time = time.time()
    export_to_csv = highscore(start_time, end_time)
    save_highscore(export_to_csv)
    highscore_table = read_highscore()
    print_highscore(highscore_table)


if __name__ == "__main__":
    main()
