import os
from time import time, strftime
from text import *
from game_start import *
from game_inventory import *
from game_menu import *
from hotncold import *
from riddles import *


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


def create_board(filename='stage1.txt'):

    board = []
    current_board = open(filename).readlines()
    for line in current_board:
        board.append(list(line.strip()))
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
                print(colours.Purple + '⛰️' + colours.Barier, end='')
            elif char == '%':
                print(colours.Red + char + colours.Barier, end='')
            elif char == 'P':
                print(background.blue + colours.Blue + char + colours.Barier, end='')
            else:
                print(colours.Green + char + colours.Barier, end='')
        print(end='\n')
    print(print_table(inventory))


def insert_player(board, x, y):

    board[y][x] = "@"
    return board


def collect_elements(stage_item):

    elements = ['%', '*', '+', '&']

    if stage_item == elements[0]:
        inventory['fuel'] += 50
    elif stage_item == elements[1]:
        inventory['Platyna'] += 10
    elif stage_item == elements[2]:
        inventory['Iryd'] += 10
    elif stage_item == elements[3]:
        inventory['Pallad'] += 10
    suma = (inventory['Platyna'], inventory['Pallad'], inventory['Iryd'])
    if sum(suma) == 300:
        inventory['Weapons'] = 1
        inventory['Pallad'] = 0
        inventory['Platyna'] = 0
        inventory['Iryd'] = 0


def change_board(board_char):

    board = None
    if board_char == '8':
        board = create_board('boss_map.txt')
    elif board_char == '9':
        board = create_board('maze_board2.txt')
    elif board_char == '7':
        board = create_board('maze_board.txt')
    elif board_char == '1':
        board = create_board('stage1.txt')
    elif board_char == '0':
        board = create_board('stage1.txt')
    elif board_char == 'P':
        hot_cold()
        game_end()
    return board


def move_player(x, y):

    pressed_key = getch().lower()
    current_x = x
    current_y = y
    if pressed_key == 'a':
        current_x -= 1
        inventory['fuel'] -= 1
    elif pressed_key == "d":
        current_x += 1
        inventory['fuel'] -= 1
    elif pressed_key == "w":
        current_y -= 1
        inventory['fuel'] -= 1
    elif pressed_key == "s":
        current_y += 1
        inventory['fuel'] -= 1
    elif pressed_key == "x":
        game_end()

    return [current_x, current_y]

def main():

    #print_menu()
    #welcome_screen()
    start_time = time.time()
    board = create_board('stage1.txt')
    board_copy = create_board('stage1.txt')
    x = 5
    y = 5
    walls = ['#', '''\'''', '/', '|', '-', 'U', 'k', 'l', 'a', 'd', 'r', 'e', 'p', 'H', 'u', 's', 'F']
    while True:
        player_position = move_player(x, y)
        if inventory['fuel'] < 1:
            break
        if board[player_position[1]][player_position[0]] not in walls:
            board_char = board[player_position[1]][player_position[0]]
            board[player_position[1]][player_position[0]] = "@"
            board[y][x] = ' '
            x = player_position[0]
            y = player_position[1]
            if board_char in ['9', '7', '0', '1', 'P']:
                board = change_board(board_char)
            if board_char == '8':
                if inventory['Weapons'] == 1:
                    board = change_board(board_char)
                else:
                    board[y][x] = '8'
        collect_elements(board_char)
        os.system('clear')
        print_board(board)
    os.system('clear')
    print(lose)


if __name__ == "__main__":
    main()
