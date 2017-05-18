import os
import time
from text import *
from game_start import *
from game_inventory import inventory, print_table
from game_menu import print_menu
from read_key import getch
from hotncold import game_hot_cold
from riddles import guess_digit, ask_quesion
from highscore import *
from color import *


def create_board(filename='stage1.txt'):

    board = []
    with open(filename) as txtfile:
        current_board = txtfile.readlines()
        for line in current_board:
            board.append(list(line.strip()))
    return board


def print_board(board):

    for row in board:
        for char in row:
            if char == '#':
                print(background.blue + colours.Blue + char + colours.Barier, end='')
            elif char == '@':
                print(colours.Blue + char, end='')
            elif char == '8':
                print(background.cyan + colours.Yellow + char + colours.Barier, end='')
            elif char == '9':
                print(background.cyan + colours.Yellow + char + colours.Barier, end='')
            elif char == '1':
                print(background.cyan + colours.Yellow + char + colours.Barier, end='')
            elif char == '0':
                print(background.cyan + colours.Yellow + char + colours.Barier, end='')
            elif char == '7':
                print(background.cyan + colours.Yellow + char + colours.Barier, end='')
            elif char == '*':
                print(background.lightgrey + '⛰️' + colours.Barier, end='')
            elif char == '%':
                print(colours.Red + char + colours.Barier, end='')
            elif char == '<':
                print(colours.Red + char + colours.Barier, end='')
            elif char == '>':
                print(colours.Red + char + colours.Barier, end='')
            elif char == '(':
                print(colours.Red + char + colours.Barier, end='')
            elif char == ')':
                print(colours.Red + char + colours.Barier, end='')
            elif char == 'P':
                print(background.lightgrey + colours.Blue + char + colours.Barier, end='')
            else:
                print(colours.Green + char + colours.Barier, end='')
        print(end='\n')
    print(print_table(inventory))


def collect_elements(board_char):

    elements = ['%', '*', '+', '&', 'K', 'L']

    if board_char == elements[0]:
        inventory['fuel'] += 50
    elif board_char == elements[1]:
        inventory['Platinum'] += 10
    elif board_char == elements[2]:
        inventory['Iridium'] += 10
    elif board_char == elements[3]:
        inventory['Palladium'] += 10
    elif board_char == elements[-1]:
        inventory['Part1'] = 1
    elif board_char == elements[-2]:
        inventory['Part2'] = 1
    elements_sum = (inventory['Platinum'], inventory['Palladium'], inventory['Iridium'])
    weapon_parts = (inventory['Part2'] + inventory['Part1'])
    if sum(elements_sum) >= 300 and weapon_parts == 2:
        inventory['Weapons'] = 1
        inventory['Palladium'] = 0
        inventory['Platinum'] = 0
        inventory['Iridium'] = 0
        inventory['Part1'] = 0
        inventory['Part2'] = 0


def change_board(board_char):

    board = None
    if board_char == '8':
        inventory['Level'] = 4
        board = create_board('boss_map.txt')
    if board_char == '9':
        inventory['Level'] = 2
        board = create_board('maze_board2.txt')
    if board_char == '7':
        inventory['Level'] = 3
        board = create_board('maze_board.txt')
    if board_char == '1':
        guess_digit()
        board = create_board('stage1.txt')
    if board_char == '0':
        ask_quesion()
        board = create_board('stage1.txt')

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


    obstacles = [
                '#', '.', '/', '(', ')', '|', 'o', '=', '-', 'U', 'k', 'n',
                'l', 'a', 'd', 'r', 'e', 'p', 'H', 'u', 's', 'F', 'i'
                ]
    print_menu()
    welcome_screen()
    start_time = time.time()
    board = create_board('stage1.txt')
    board_copy = create_board('stage1.txt')
    x = 5
    y = 5
    print_board(board)
    while True:

        player_position = move_player(x, y)
        if inventory['fuel'] < 1:
            os.system('clear')
            print(lose)
            break
        if board[player_position[1]][player_position[0]] not in obstacles:
            board_char = board[player_position[1]][player_position[0]]
            board[player_position[1]][player_position[0]] = "@"
            board[y][x] = ' '
            x = player_position[0]
            y = player_position[1]
            if board_char == '!':
                inventory['Armor'] -= 1
            if board_char in ['0', '1']:
                board = change_board(board_char)
            elif board_char == '9':
                board = change_board(board_char)
            elif board_char == '7':
                board = change_board(board_char)
            elif board_char == '8':
                if inventory['Weapons'] == 1:
                    board = change_board(board_char)
            elif board_char == 'P':
                os.system('clear')
                game_hot_cold()
                break
        collect_elements(board_char)
        os.system('clear')
        print_board(board)

    end_time = time.time()
    time_game = end_time - start_time
    time.sleep(4)
    os.system('clear')
    add_highscore(time_game)


if __name__ == "__main__":
    main()
