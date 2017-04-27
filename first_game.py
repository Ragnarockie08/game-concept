import os
from math import fabs
from text import welcom, end
import time
import sys, tty, termios


def main_stage(board):
    row = []
    board = []
    text = open('board.txt').readlines()
    for line in text:
        for char in line:
            row.append(char)
        board.append(row)
        row = []

    for line in board:
        line[-1] = line[-1].strip()

    return board


def print_board(fuel, board):

    for row in board:
        print("".join(row))
    print("Fuel: {}".format(fuel))


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


def fuel_down(fuel):

    fuel -= 2
    return fuel


def move_player(board, x, y):

    pressed_key = getch()
    if pressed_key == 'w' and board[y - 1][x] != '#':
        y -= 1
    elif pressed_key == 's' and board[y + 1][x] != '#':
        y += 1
    elif pressed_key == 'a' and board[y][x - 1] != '#':
        x -= 1
    elif pressed_key == 'd' and board[y][x + 1] != '#':
        x += 1
    elif pressed_key == 'x':
        x = 'exit'
    return x, y


def welcome():

    os.system('clear')
    print(welcom)
    start = input("press S to start the game or Q to quit")
    if start.lower() == "q":
        game_end()


def game_end():

    os.system('clear')
    print(end)
    print("Thanks for playing and see you next time")
    time.sleep(2)
    sys.exit()


def main():

    fuel = 300
    x = 1
    y = 5
    board = []

    welcome()
    while x != "exit":
        os.system('clear')
        board = main_stage(board)
        board = insert_player(board, x, y)
        print_board(fuel, board)
        x, y = move_player(board, x, y)




if __name__ == "__main__":
    main()
