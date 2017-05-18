import random
from game_inventory import inventory
import time

def guess_digit():
    random_digit = range(0, 10)
    random_digit = str(random.choice(random_digit))
    print(random_digit)

    print("Guess digit. From 0 into 10.")

    while True:
        if inventory['Armor'] < 1:
            print(lose)
        tries = 1
        print('Guess #', tries)
        guess_digit = input("Guess a digit: ")
        if guess_digit > random_digit:
            print("Too much")
            inventory['Armor'] -= 1
            continue
        elif guess_digit < random_digit:
            print("Too little")
            inventory['Armor'] -= 1
            continue
        else:
            break
        tries += 1



def test_milk_galaxy():
    question_list = ["aaa? ", "bbb? ", "ccc? ", "ddd? "]
    answer_list = ["1", "2", "3", "4"]

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
