import datetime
import csv

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

        sorted_desc = sorted(score, key=lambda x: x[2]) #Sorts desc
        print(longest_name)
        space = (" " * 10)


        print("HIGHSCORE")
        print("name".rjust(longest_name), "date".rjust(6), "time".rjust(6))
        print("-" * (longest_name + 15))
        for item in sorted_desc:
            print(item[0].rjust(longest_name), item[1], space,  item[2])
            # print(" ".join(item[0], str(item[1]), str(item[2])))
            # print(" ".join(item))
        print("-" * (longest_name + 15))


#
#
# def add_highscore(time):
#     username = input("Enter your username: ")
#     now = datetime.datetime.now()
#
#     file_csv = open('highscore.csv', "a")
#     file_csv.write(username + "|" + str(now) + "|" + str(time) + "|" +'\n')
#     file_csv.close()
#     show_highscore()



show_highscore()
