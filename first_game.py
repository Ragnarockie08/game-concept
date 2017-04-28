import os
import time
import sys, tty, termios
from text import welcom, end
from colored import fg, bg, attr


red = fg('red')
reset = attr('reset')
file_name = 'board.txt'


def main_stage(board):
    row = []
    board = []

    text = open(file_name, "r").readlines()
    for line in text:
        for char in line:
            if char == "#":
                char = red + char + reset
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
    if pressed_key == 'w' and board[y - 1][x] == ' ':
        y -= 1
    elif pressed_key == 's' and board[y + 1][x] == ' ':
        y += 1
    elif pressed_key == 'a' and board[y][x - 1] == ' ':
        x -= 1
    elif pressed_key == 'd' and board[y][x + 1] == ' ':
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
    start = input("press S to start the game or Q to quit")
    if start.lower() == "q":
        x = "exit"
        game_end()

'''def change_board(board):
    if '''

def game_end():

    os.system('clear')
    print(end)
    print("Thanks for playing and see you next time")
    time.sleep(2)
    sys.exit()


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
