import random

def guess_digit():
    random_digit = range(0, 10)
    random_digit = str(random.choice(random_digit))
    print(random_digit)

    print("Guess digit. From 0 into 10.")

    while True:
        tries = 1
        print('Guess #', tries)
        guess_digit = input("Guess a digit: ")
        if guess_digit > random_digit:
            print("Too much")
            continue
        elif guess_digit < random_digit:
            print("Too little")
            continue
        else:
            break
    print("You right. Welcome in the huhu")


def test_milk_galaxy():
    question_list = ["aaa? ", "bbb? ", "ccc? ", "ddd? "]
    answer_list = ["1", "2", "3", "4"]

    random_digit = range(0, 4)
    random_digit = random.choice(random_digit)
    tries = 3

    while True:
        guess = input("".join([question_list[random_digit]]))

        if guess == answer_list[random_digit]:
            print("Cool. Welcome in main Galaxy")
            break
        else:
            tries -= 1
            if tries < 0:
                print("Lose")
            print("Try again. You have tries: " , tries)
            continue

    print("aaaa")




# guess_digit()
test_milk_galaxy()
