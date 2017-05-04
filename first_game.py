import os
import time
import sys, tty, termios
from text import welcom, end
from colored import fg, bg, attr
from game_start import choose_spaceship, skip, clear, game_end

colors = {'green': bg('green') + fg('green'), 'red': bg('red') + fg('red'), 'blue': fg('blue'), 'black': bg('black') + fg('black'),
          'reset': attr('reset')}


def main_stage(board):
    file_name = 'stage1.txt'
    row = []
    board = []

    text = open(file_name, "r").readlines()
    for line in text:
        for char in line:
            if char == "#":
                char = colors['red'] + char + colors['reset']
            if char.isalpha():
                char = colors['blue'] + char + colors['reset']
            row.append(char)
        board.append(row)
        row = []

    for line in board:
        line[-1] = line[-1].strip()

    return board


def print_board(board):

    for row in board:
        print("".join(row))


def insert_player(fuel, board, x, y):

    board[y][x] = "@"
    return board

'''def insert_alien(board, x, y):
    board[y][x] = "O"
    return board'''

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
    if pressed_key == 'w' and board[y - 1][x] == ' ' or board[y - 1][x] == '8':
        y -= 1
    elif pressed_key == 's' and board[y + 1][x] == ' ' or board[y + 1][x] == '8':
        y += 1
    elif pressed_key == 'a' and board[y][x - 1] == ' ' or board[y][x - 1] == '8':
        x -= 1
    elif pressed_key == 'd' and board[y][x + 1] == ' ' or board[y][x + 1] == '8':
        x += 1
    elif pressed_key == 'x':
        x = "exit"
        game_end()
    print(fuel_down(fuel))

    return x, y


'''def move_alien(board, x_a, y_a):

    pressed_key = getch()
    if pressed_key == 'd' and board[y_a][x_a - 1] == ' ':
        x_a += 1
    elif pressed_key == 'w' and board[y_a][x_a + 1] == ' ':
        x_a -= 1
    elif pressed_key == 's' and board[y_a + 1][x_a] == ' ':
        y_a -= 1
    elif pressed_key == 'x' and board[y_a - 1][x_a] == ' ':
        y_a += 1

    return x_a, y_a'''


def welcome():

    os.system('clear')
    print(welcom)
    skip()
    choose_spaceship()
    skip()

'''def change_board(board):
    if '''


def main():

    x = 1
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
