import random
from game_inventory import inventory
import time
from text import lose
from game_start import game_end

def guess_digit():

    random_digit = range(0, 10)
    random_digit = str(random.choice(random_digit))
    print(random_digit)

    print("Guess digit. From 0 into 10.")
    tries = 1
    while True:
        print("="* 40)
        if inventory['Armor'] < 1:
            print(lose)
            add_highscore()
            time.sleep(5)
            sys.exit()
        print('Guess #', tries)
        guess_digit = input("Guess a digit: ")
        if guess_digit.isalpha():
            print("Wrong input")
        elif guess_digit > random_digit:
            print("Too much")
            inventory['Armor'] -= 1
            tries += 1
            continue
        elif guess_digit < random_digit:
            print("Too little")
            inventory['Armor'] -= 1
            tries += 1
            continue
        else:
            break


def ask_quesion():

    question_list = ["Which one is Earth from the Sun in Solar System? ", "How many stars are in the Solar System?",
    "How many moons does Earth have? ", "How many moons does Mars have? "]
    answer_list = ["3", "1", "1", "2"]

    random_digit = range(0, 4)
    random_digit = random.choice(random_digit)

    while True:
        guess = input("".join([question_list[random_digit]]))

        if guess == answer_list[random_digit]:
            print("Cool. Welcome in main Galaxy")
            break
        else:
            inventory['Armor'] -= 1
            if inventory['Armor'] < 0:
                print(lose)
                add_highscore()
                time.sleep(5)
                sys.exit()
