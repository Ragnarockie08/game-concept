import random
import os
import sys
import time
from game_inventory import inventory
from text import lose, win, boss_fight

def game_hot_cold():
    print_instruction()
    random_digit = draw_digits()
    print(random_digit)

    random_digit_list = list(random_digit)
    tries = 1

    while True:
        count_hot = 0
        count_warm = 0
        count_cold = 0
        print('Guess #', tries)

        digit_input = guess_digit()
        digit_input_list = check_digis(digit_input, random_digit_list)

        tries += 1

        if inventory['Armor'] == -1:
            os.system('clear')
            print(lose)
            time.sleep(2)
            break

        if digit_input_list == random_digit_list:
            os.system('clear')
            print(win)
            break



def print_instruction():
    print('I am thinking of a 3-digit number. Try to guess what it is.\n\
          Here are some clues:\n\
          When I say:    That means:\n\
          Cold       No digit is correct.\n\
          Warm       One digit is correct but in the wrong position.\n\
          Hot        One digit is correct and in the right position.\n\
          I have thought up a number. You have 10 guesses to get it.')


def draw_digits():
    random_digit = range(100, 1000)
    random_digit = str(random.choice(random_digit))
    return random_digit


def guess_digit():
    digit_input = 0
    while True:
        try:
            digit_input = int(input("Guess digit: "))
        except ValueError:
            print("Try again. Enter 3 digits.")
            continue

        if len(str(digit_input)) != 3:
            print("Try again. Enter 3 digits.")
            continue
        else:
            break
    return str(digit_input)


def check_digis(digit_input, random_digit_list):
    count_hot = 0
    count_warm = 0
    count_cold = 0

    digit_input_list = list(digit_input)
    index_of_hot = []
    for item in range(len(digit_input_list)):
        if digit_input_list[item] == random_digit_list[item]:
            count_hot += 1
            index_of_hot.append(item)

    list_to_check_warm = [0, 1, 2]
    for i in range(len(index_of_hot)):
        list_to_check_warm.remove(index_of_hot[i])

    for i in list_to_check_warm:
        if digit_input_list[i] in random_digit_list:
            count_warm += 1
        else:
            count_cold += 1
    if count_cold == 3:
        print("Cold")
        inventory['Armor'] -= 1
    else:
        print("Hot " * count_hot, " Warm " * count_warm)
        inventory['Armor'] -= 1
    print("Armor: {}".format(inventory['Armor']))

    return digit_input_list
