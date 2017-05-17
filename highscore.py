import datetime
import csv

def show_highscore():
    with open('highscore.csv', encoding='utf-8-sig') as csvfile:
        reader = csvfile.readlines()
        score = []

        spilit_score = [line.split(" | ") for line in reader]

        for row in spilit_score:
            # name = (row[0], row[1])
            # information = (row[2], row[3], row[4].replace('\n', ''))

            score.append(row)



    # print(score)
    #



def add_highscore(time):
    username = input("Enter yout username!")
    now = datetime.datetime.now()

    with open('highscore.csv', 'a') as csv_file:
        wiriter = csv.writer(csv_file)

    file_csv = open('highscore.csv', "a")
    file_csv.write(username + " | " + str(now) + " | " + str(time) + "  | " +'\n')

    show_highscore()
