import os
from math import fabs

def create_main_board(width, height):

    board = []
    counter = width - 2
    limit = height -1
    for row in range(height):
        board.append([])
        for column in range(width):
            board[row].append("#")
    for digit in range(1, limit):
        board[digit][1:-1] = ' ' * counter

    '''planet1(board)
    y = 2
    x = 7
    counter = int(fabs(y-x))

    board[4][y:x] = "#" * counter'''
    return board

'''def planet1(board):
    y = 10
    x = 13
    counter = int(fabs(y-x))
    board[4][y:x] = "#" * counter
    for x, y in board:
        print("#")
        if x > board[1][-1] and y > board[1][-1]:
            print(".")
    board[5][9] = "#"
    board[5][13] = "#"
    board[6][9] = "#"
    board[6][13] = "#"
    board[7][10] = "#"
    board[7][10] = "#"
    board[5][11] = "8"'''


def print_board(fuel, board):

    for row in board:
        print("".join(row))
    print("Fuel: {}".format(fuel))



def insert_player(board, x, y):
    board[y][x] = "@"

def getch():
    import sys, tty, termios
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


def main():

    fuel = 300
    x = 1
    y = 5

    while x != "exit" or fuel > 0:
        os.system('clear')
        board = create_board(80, 20)
        insert_player(board, x, y)
        print_board(fuel, board)
        x, y = move_player(board, x, y)
        fuel_down(fuel)



if __name__ == "__main__":
    main()
