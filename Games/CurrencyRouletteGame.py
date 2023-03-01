import random
import requests



def get_money_interval(difficulty,dollar):
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    response = requests.get(url)
    data = response.json()
    ils_rate = data['rates']['ILS']
    nis = round((dollar * ils_rate), 2)
    interval = (nis - (5 - difficulty), nis + (5 - difficulty))
    return interval

def get_guess_from_user(dollar):
    while True:
        guess = input(f'Try to convert this: {dollar}$ to NIS(₪) - ')
        if guess.replace('.', '', 1).isdigit():
            guess = float(guess)
            break
        print("Invalid input, you must enter a number")

    return guess

def play(difficulty):
    dollar = random.randint(1,100)
    interval = get_money_interval(difficulty,dollar)
    guess = get_guess_from_user(dollar)
    if interval[0] <= guess <= interval[1]:
        print('Congratulations! You have successfully guessed the amount of money')
        return True
    else:
        print('ohh... try next time')
        return False


