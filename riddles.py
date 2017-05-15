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



def test_milk_galaxy:
    

# guess_digit()
test_milk_galaxy()
