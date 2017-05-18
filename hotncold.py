import random
import os
import sys
import time
from game_inventory import inventory
from text import lose, win, boss_fight



def hot_cold():
    print(boss_fight)
    random_digit = range(100, 1000)
    random_digit = str(random.choice(random_digit))
    print_rules()


def print_rules():

    tries = 1
    while True:
        print('I am thinking of a 3-digit number. Try to guess what it is.\n\
              Here are some clues:\n\
              When I say:    That means:\n\
              Cold       No digit is correct.\n\
              Warm       One digit is correct but in the wrong position.\n\
              Hot        One digit is correct and in the right position.\n\
              I have thought up a number. You have {} guesses to get it.'.format(inventory['Armor']))

        random_digit = range(100, 1000)
        random_digit = str(random.choice(random_digit))
        print(random_digit)

        tries = 1
        digit_input = input("Guess digit: ")
        while inventory['Armor'] > 0:
            print('Guess #', tries)
            if tries == 1:
                pass
            else:
                digit_input = input("Guess digit: ")

            list_random = [random_digit[0], random_digit[1], random_digit[2]]
            list_input = [digit_input[0], digit_input[1], digit_input[2]]
            index_of_hot = []
            count_hot = 0
            count_warm = 0
            count_cold = 0

            for i in range(len(list_input)):
                if list_input[i] == list_random[i]:
                    count_hot += 1
                    index_of_hot.append(i)

            list_to_check_warm = [0, 1, 2]
            for i in range(len(index_of_hot)):
                list_to_check_warm.remove(index_of_hot[i])

            for i in list_to_check_warm:
                if list_input[i] in list_random:
                    count_warm += 1
                else:
                    count_cold += 1
            if count_cold == 3:
                print("Cold")
                inventory['Armor'] -= 1
                print("Armor: ", inventory['Armor'])
            else:
                print("Hot " * count_hot, " Warm" * count_warm)
                inventory['Armor'] -= 1
                print("Armor: ", inventory['Armor'])


            tries += 1

            if digit_input == random_digit:
                os.system('clear')
                print(win)
                print('''                                                                                  Armor left: {}'''.format(inventory['Armor']))
                break
            elif inventory['Armor'] < 1:
                time.sleep(2)
                os.system('clear')
                print(lose)
                time.sleep(2)
        break
