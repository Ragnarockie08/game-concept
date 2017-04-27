import os
import time
import sys, tty, termios
from text import welcom, end
from colored import fg, bg, attr


grey = bg('grey_19') + fg('grey_19')
reset = attr('reset')

def main_stage(board):
    row = []
    board = []
    text = open('board.txt', "r").readlines()
    for line in text:
        for char in line:
            if char == "#":
                char = grey + char + reset
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
    return fuel


def move_player(board, x, y):

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


def game_end():

    os.system('clear')
    print(end)
    print("Thanks for playing and see you next time")
    time.sleep(2)
    sys.exit()


def main():

    fuel = 300
    x_a = 5
    y_a = 7
    x = 1
    y = 5
    board = []

    welcome()
    while x != "exit":
        os.system('clear')
        board = main_stage(board)
        '''board = insert_alien(board, x_a, y_a)'''
        board = insert_player(board, x, y)
        print_board(fuel, board)
        x, y = move_player(board, x, y)


if __name__ == "__main__":
    main()
