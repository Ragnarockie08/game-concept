import datetime
import csv
from first_game import time
from text import highscore, title

def show_highscore():
    with open('highscore.csv', encoding='utf-8-sig') as csvfile:
        reader = csvfile.readlines()
        score = []
        longest_name = 0
        count = 0
        count_highscore = 1

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

        print(title)
        print(highscore)
        print("PLACE".rjust(80), "NAME".rjust(longest_name + 4), "DATE".rjust(14), "TIME".rjust(13))
        print(("-" * (longest_name + 60)).rjust(130))
        for item in sorted_desc:
            print(str(count_highscore).rjust(80), "".join((item[0].rjust(longest_name + 4), item[1][:10].rjust(15), item[2][:4].rjust(10), " sec")))
            count_highscore += 1
        print(("-" * (longest_name + 60)).rjust(130))

def add_highscore(time):
    username = input("Enter your username: ")
    now = datetime.datetime.now()

    file_csv = open('highscore.csv', "a")
    file_csv.write(username + "|" + str(now) + "|" + str(time) + "|" +'\n')
    file_csv.close()
    show_highscore()
