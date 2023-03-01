import random


def gener_number(difficulty):
    secret_number = int(random.randint(1, difficulty))
    return secret_number


def get_guess_from_user(difficulty):
    while True:
        guess = input(f'guess a number between 1 - {difficulty}:')
        if guess.isdigit():
            guess = int(guess)
            if 0 < guess < difficulty+1:
                return guess





def compare_results(guess, secret_number):
    return guess == secret_number

def play(difficulty):
    secret_number = gener_number(difficulty)
    guess = get_guess_from_user(difficulty)
    compare_results(guess, secret_number)
    result = compare_results(guess, secret_number)
    if result:
        print("Congratulations! What a lucky guess.")
        return True
    else:
        print("Sorry, maybe next time")
        return False
