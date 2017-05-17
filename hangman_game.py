import random
import sys
import os
import time


HANGMAN = [
    '''
  -----+
  |    |
       |
       |
       |
       |
-------+''',
    '''
  -----+
  |    |
  O    |
       |
       |
       |
-------+''',
    '''
  -----+
  |    |
  O    |
  |    |
       |
       |
-------+''',
    '''
  -----+
  |    |
  O    |
 /|\   |
       |
       |
-------+''',
    '''
  -----+
  |    |
  O    |
 /|\   |
 /     |
       |
-------+''',
    '''
  -----+
  |    |
  O    |
 /|\   |
 / \   |
       |
-------+''']


def print_hangman(life):
    '''This function, after you loose life, will print a part of hangman '''

    print(HANGMAN[5 - life])


def give_hint(life, countries):
    '''This function, when you have 3 lives left, will print a hint '''

    if life <= 3:
        print("This city is capital of {}".format(countries[0]))


def print_information(life, not_in_word):
    '''This function, shows bad letters that user guessed and lives left '''

    print("=" * 40)  # this print is making nice breaker beetwen other prints
    print("Bad guesses: ", not_in_word)
    print("")  # free line
    print("Lifes left: {}".format(life))
    print("")


def print_dashes(guessed_word, good_guesses):
    '''This function, replace letters in oryginal word by dashes '''

    # this loop sets dashes and letters
    # in right place considering if there is space beetwen words
    for letter in guessed_word:
        if letter in good_guesses:
            print(letter.upper(), end="")
        elif letter != " ":
            print("_", end="")
        else:
            print(" ", end="")

    print("")


def win_process(countries, guessed_word, good_guesses, not_in_word, start_time):
    '''This function start when hidden word is guessed. It print congrats, print time of game and amount of guesses '''

    end_time = time.time() - start_time  # stoping timer
    print("")
    print("Congratulations! The capital city of {} is {}.".format(countries[0], guessed_word))
    print("")
    username = input("Type in your username: ")
    os.system('clear')
    tries = len(good_guesses + not_in_word)
    print(
        "{} | {} | Time: {} sec | Guesses: {} | {}".format(
            username,
            time.asctime(),
            int(end_time),
            tries + 1,
            guessed_word))
    print("")


def lose_process(countries, guessed_word):
    '''This function start when user run out of his lives. It prints a hidden word. '''

    print(HANGMAN[5])
    print("=" * 40)
    print("Sorry but you run out of lifes!")
    print("The capital of {} is {}".format(countries[0], guessed_word))
    print("")


def ask_play_again():
    '''This function ask the user if he want to play again or quit game '''

    again = input("Press Y to play again or Q to quit")
    if again.lower() == "q":
        print("")
        print("Thanks for playing !")
        sys.exit()


def main():

    start = True
    while start:

        # in this lines is making list from the file of countries and their capitals
        caplist = []
        with open('c_a_c.txt') as capitals:
            for line in capitals:
                inner_list = [capital.strip() for capital in line.split(',')]
                caplist.extend(inner_list)

        # defining lists and secret word necessary for program properly working
        countries = random.choice(caplist).split(' | ')
        os.system('clear')
        start_time = time.time()  # starting_timer
        guessed_word = countries[1].upper()
        life = 5
        not_in_word = []
        good_guesses = []

        while life > 0:

            print_hangman(life)

            give_hint(life, countries)

            print_information(life, not_in_word)

            print_dashes(guessed_word, good_guesses)

            guess = input("Please enter letter or whole word:  ").upper()
            print("=" * 40)

            if not guess.replace(" ", "").isalpha():
                os.system('clear')
                print("You can only guess letters!")

            elif guess in good_guesses or guess in not_in_word:
                os.system('clear')
                print("You already guessed that letter/word!")

            elif len(guess) == 1:

                if guess in guessed_word:
                    os.system('clear')
                    good_guesses.append(guess)
                else:
                    os.system('clear')
                    print("Sorry this letter is not in this word!")
                    not_in_word.append(guess)
                    life -= 1

            elif guess == guessed_word:
                os.system('clear')
                win_process(countries, guessed_word, good_guesses, not_in_word, start_time)
                ask_play_again()
                start = True
                break

            else:
                life -= 2
                not_in_word.append(guess)
                os.system('clear')
                print("Sorry thats not right word")
                continue

        # this else happend when player loses his all lifes.
        else:
            os.system('clear')
            lose_process(countries, guessed_word)
            ask_play_again()
            start = True


main()
