from Games import GuessGame
from Games import MemoryGame
from Games import CurrencyRouletteGame
from ScoreFile import Score
import os
from ScoreFile import Utils


# this function take the user_name input and return a string "welcome..."
def welcome():
    name = input("enter your name:")
    print(f'Hello {name} and welcome to the World of Game (WoG).\nHere you can find many cool games to play.')
    return
# this function take the chosen input and check what the user want to play and get the difficulty of the game


def load_game():
    game_types = {1: 'MemoryGame', 2: 'GuessGame', 3: 'CurrencyRoulette'}
    difficulties = {1: 'Beginner', 2: 'Amateur', 3: 'Semi-Pro', 4: 'Professional', 5: 'World Class'}
    while True:

        game_input = input("""Please choose a game to play:

        1. Memory Game - a sequence of numbers will appear for 1 second and you have to
        guess it back
        2. Guess Game - guess a number and see if you chose like the computer
        3. Currency Roulette - try and guess the value of a random amount of USD in ILS
        """)
        if game_input.isdigit():
            game_type = int(game_input)
            if game_type >= 1 and game_type <= 3:
                game = game_types[game_type]
                break
            else:
                print("Invalid input, you must select a game between 1 and 3")
        else:
            print("Invalid input, you must enter a number between 1 and 3")

    while True:
        difficulty_input = input("""Please choose game difficulty (1-5):
         1: Beginner
         2: Amateur 
         3: Semi-Pro 
         4: Professional
         5: World Class
         """)
        if difficulty_input.isdigit():
            difficulty_of_game = int(difficulty_input)
            if difficulty_of_game >= 1 and difficulty_of_game <= 5:
                difficulty = difficulties[difficulty_of_game]
                break
            else:
                print("Invalid input, you must select a difficulty between 1 and 5")
        else:
            print("Invalid input, you must enter a number between 1 and 5")

    print(f'Nice choice! Prepare to play {game} in {difficulty} difficulty.')
    current_score = "0"
    if game_type == 1:
        is_winner = MemoryGame.play(difficulty_of_game)
        if is_winner:
            current_score = Score.add_score(difficulty_of_game)
    if game_type == 2:
        is_winner = GuessGame.play(difficulty_of_game)
        if is_winner:
            current_score = Score.add_score(difficulty_of_game)
    if game_type == 3:
        is_winner = CurrencyRouletteGame.play(difficulty_of_game)
        if is_winner:
            current_score = Score.add_score(difficulty_of_game)
    while True:
        user_answer = input("You want to play again [YES/NO]? ")
        if user_answer.lower() == 'yes':
            print(f"Your score for now is :{current_score}")
            load_game()
            break
        elif user_answer.lower() == 'no':
            print('See you next time')
            os.system('python3 ../ScoreFile/MainScores.py')
            os.remove(Utils.SCORES_FILE_NAME)
            break
        else:
            print('Invalid input, you must enter YES/NO')
