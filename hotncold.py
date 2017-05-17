import random


def show_description():
    print('\033[1;1;1m' + "{}".format('I am thinking of a 3-digit number. Try to guess what it is.\n') +
          '\033[0m')
    print('Here are some clues:')
    print('{:^10}{:^20}'.format('When I say:', 'That means:'))
    print('{:^10}{:^20}'.format('Cold', 'No digit is correct.'))
    print('{:^10}{:^20}'.format('Warm', 'One digit is correct but in the wrong position.'))
    print('{:^10}{:^20}'.format('Hot', 'One digit is correct and in the right position.'))
    print('\033[1;30;1m' + "{}".format('I have thought up a number. You have 10 guesses to get it.\n') +
          '\033[0m')


def draw_digit():
    random_digit = range(100, 1000)
    random_digit = str(random.choice(random_digit))
    print(random_digit)
    return random_digit

def game(random_digit):
    tries = 1
    count_hot = 0
    count_warm = 0
    count_cold = 0
    list_random = []
    list_digit = []
    index_of_hot = []

    for item in random_digit:
        list_random.append(item)

    while True:
        print("\n")
        digit_input = input("\033[92mGuess digit:\033[0m ")
        print('Guess #', tries)

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
        else:
            print("Hot " * count_hot," Warm" * count_warm)

        tries += 1

        if list_random == list_input:
            break
    print('\033[93mYou got it!')



def main():
    show_description()
    digit = draw_digit()
    game(digit)


main()
