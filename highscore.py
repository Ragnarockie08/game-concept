import datetime
import csv
from first_game import *

def show_highscore():
    with open('highscore.csv', encoding='utf-8-sig') as csvfile:
        reader = csvfile.readlines()
        score = []
        longest_name = 0
        count = 0

        spilit_score = [line.split("|") for line in reader]

        for row in spilit_score:
            score.append((row[0], row[1], row[2].replace("\n", "")))

        for item in score:
            lenght_name = len(item[0])
            if count == 0:
                longest_name = lenght_name
            else:
                if lenght_name > longest_name:
                    longest_name = lenght_name
            count += 1

        sorted_desc = sorted(score, key=lambda x: x[2])

        print("HIGHSCORE")
        print("name".rjust(longest_name), "date".rjust(15), "time".rjust(6))
        print("-" * (longest_name + 30))
        for item in sorted_desc:
            print("".join((item[0].rjust(longest_name), item[1][:10].rjust(15), item[2][:4].rjust(6), " sec")))
        print("-" * (longest_name + 30))

#

def add_highscore(time):
    username = input("Enter your username: ")
    now = datetime.datetime.now()

    file_csv = open('highscore.csv', "a")
    file_csv.write(username + "|" + str(now) + "|" + str(time) + "|" +'\n')
    file_csv.close()
    show_highscore()

#

show_highscore()
