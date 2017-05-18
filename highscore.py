import datetime
import csv
from text import highscore, title
from color import *
from game_inventory import Inventory


def write_highscore():
    with open('highscore.csv', encoding='utf-8-sig') as csvfile:
        reader = csvfile.readlines()
        score_list = []

        spilit_score = [line.split("|") for line in reader]

        for row in spilit_score:
            score_list.append((row[0], row[1], row[2], row[3].replace("\n", "")))

        sorted_list = sorted(score_list, key=lambda x: int(x[3]), reverse = True)
        sorted_list = sorted(sorted_list, key=lambda x: float(x[2]))
        longest_name = count_longest_name(score_list)
        print_highscore(sorted_list, longest_name)


def add_highscore(time):

    inventory = Inventory()
    while True:
        username = input("Enter your username: ")
        if len(username) > 10:
            print("Wrong input")
        else:
            break

    now = datetime.datetime.now()
    file_csv = open('highscore.csv', "a")
    file_csv.write(username + "|" + str(now) + "|" + str(time) + "|" +  str(inventory['Level']) +'\n')
    file_csv.close()

    write_highscore()



def print_highscore(sorted_list, longest_name):
    count_highscore = 1
    print(title)
    print(highscore)
    print(colours.Blue + "PLACE".rjust(80), colours.Yellow + "NAME".rjust(longest_name + 4),colours.Green + "DATE".rjust(14), colours.Blue +"LEVEL".rjust(9), colours.Red+"TIME".rjust(13) + colours.Barier)
    print(("-" * (longest_name + 50)).rjust(130))
    for item in sorted_list:
            print(str(count_highscore).rjust(80), "".join((item[0].rjust(longest_name + 4), item[1][:10].rjust(15), item[3].rjust(10), item[2][:4].rjust(10), " sec")))
            count_highscore += 1
    print(("-" * (longest_name + 50)).rjust(130))


def count_longest_name(score_list):
    count = 0
    longest_name = 0
    for item in score_list:
        lenght_name = len(item[0])
        if count == 0:
            longest_name = lenght_name
        else:
            if lenght_name > longest_name:
                longest_name = lenght_name
        count += 1

    return longest_name
