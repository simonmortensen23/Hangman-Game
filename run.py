# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
from words import words
from hangman_art import *
from typewriter import *
from pyfiglet import Figlet
import colorama
from colorama import init, Fore
init(autoreset=True)

def get_random_word():
    """
    This function selects and returns a random word from the words.py file
    """
    word = random.choice(words) #Chooses random word from words array
    return word

def display_current_game_status(missed_letters, correct_letters, word):
    """
    This function prints the layout of the playerboard and updates it after every turn
    """
    global lives
    player_lives = display_hangman(lives)
    #TODO: instead print the hangman picture here
    print(display_hangman(lives))

    print()
    print(f"Letters you have guessed wrong so far: ", ' '.join(missed_letters))
    print()
    placeholder_word = '_' * len(word) #Finds _ * the length of the unknown word

    for index in range(len(word)):
        if word[index] in correct_letters:
            placeholder_word = placeholder_word[:index] + word[index] + placeholder_word[index+1:]

    for letter in placeholder_word:
        print(letter, end=' ')
    print()

def take_guess_input(already_guessed):
    """
    Handles the player guess input and checks if it a single letter that has not been used yet
    """
    while True:
        guess = input("Guess a letter: ")
        print()
        guess = guess.lower()
        if len(guess) != 1:
            print("Please enter a single letter.")
        elif guess in already_guessed:
            print("You have already guessed that letter. Choose again.")
        elif guess not in "abcdefghijklmnopqrstuvwxyz":
            print("Please enter a LETTER")
        else:
            return guess
     
def ask_to_play_again():
    """
    This function asks the player if they want to play again or quit the game
    """
    play_again = input("Do you want to play again? (yes or no): ").lower()
    if play_again == "yes":
        run_game()
    else:
        print(f"Game is over {player_name}, enjoy your day!")
    
def take_user_name_input():
    """
    """
    player_name = input("Enter your name: ")
    print(f"Welcome {player_name}!")

def check_if_all_letters_are_guessed(correct_guesses, word):
    """
    """
    for i in range (len(word)):
        if word[i] not in correct_guesses:
            return False

    print("Congratulations! You have guessed the word: " + word)
    return True

def run_game():
    """
    """
    global lives
    lives  = 0
    incorrect_guess_letters = ''
    correct_letters = ''
    word = get_random_word()
    is_game_over = False

    print()

    while True:
        display_current_game_status(incorrect_guess_letters, correct_letters, word)
        guess = take_guess_input(incorrect_guess_letters + correct_letters)
        if guess in word:
            correct_letters = correct_letters + guess
            is_game_over = check_if_all_letters_are_guessed(correct_letters, word)
        else:
            lives = lives + 1
            incorrect_guess_letters = incorrect_guess_letters + guess
            if len(incorrect_guess_letters) == 7:
                display_current_game_status(incorrect_guess_letters, correct_letters, word)
                print("You are out of lives!\nAfter " + str(len(incorrect_guess_letters)) + " missed guesses and " + str(len(correct_letters)) + " correct guesses, the word was '" + word + "'")
                is_game_over = True
        if is_game_over:
            ask_to_play_again()

def print_welcome_message():
    """
    This functions prints out
    """
    f = Figlet(font='slant')
    print(f.renderText("Hangman"))
    typewriter(f"""
D O  Y O U  D A R E  T O  R I S K  Y O U R  N E C K\t\n
E N T E R   Y O U R   N A M E  T O  S T A R T  G A M E\t\n\nA N D   H A V E   F U N ! !\n""")

def display_hangman(lives):
    """
    Display hangman stages from the start of the game
    and change anytime the player doesn't guess the right letterr
    """
    return hangman_pics[lives]

def start_game():
    """
    """
    print_welcome_message()
    take_user_name_input()
    run_game()

start_game()




   