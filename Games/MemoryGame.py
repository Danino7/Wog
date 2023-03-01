import random
import time
import re
from ScoreFile.Utils import screen_cleaner
def generate_sequence(difficulty):
    random_list = random.sample(range(1, 101), difficulty)
    print(random_list, end='')
    time.sleep(0.7)
    screen_cleaner()
    return random_list


def get_list_from_user(difficulty):
    while True:
        guess = input(f"Enter {difficulty} numbers, separated by any symbol: ")
        guess = re.split('\D+', guess)

        guess_list_int = []
        for i in guess:
            if not i.isdigit():
                print(f'All entered values must be numbers.')
                break
            guess_list_int.append(int(i))

        if not i.isdigit():
            continue

        if len(guess_list_int) != int(difficulty):
            print(f'You must enter {difficulty} numbers, separated by any symbol.')
        else:
            return guess_list_int


def is_list_equal(guess_list_int, random_list):
    random_list.sort()
    guess_list_int.sort()
    return random_list == guess_list_int


def play(difficulty):
    random_list = generate_sequence(difficulty)
    guess_list_int = get_list_from_user(difficulty)
    result = is_list_equal(guess_list_int, random_list)
    if result:
        print('What a brilliant memory!')
        return True
    else:
        print('You are getting old :( , try next time')
        return False

