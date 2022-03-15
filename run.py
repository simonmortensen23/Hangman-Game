# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random



lives = 7
words = ["orangutan", "message", "breakfast"]

def get_random_word(wordList):
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
    player_lives = '_' * lives
    #TODO: instead print the hangman picture here
    print(player_lives)


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


def playerGuess(alreadyGuessed):
    """
    Handles the player guess input and checks if it a single letter that has not been used yet
    """
    while True:
        guess = input("Guess a letter: ")
        print()
        guess = guess.lower()
        if len(guess) != 1:
            print("Please enter a single letter.")
        elif guess in alreadyGuessed:
            print("You have already guessed that letter. Choose again.")
        elif guess not in "abcdefghijklmnopqrstuvwxyz":
            print("Please enter a LETTER")
        else:
            return guess

def progressBoard():
     

def playAgain():
    """
    This function asks the player if they want to play again or quit the game /// Not working
    """
    play_again = input("Do you want to play again? (yes or no): ")
    if play_again == "yes":
        gameOver = False
    else:
        print("Game is over, enjoy your day!")


def run_game():
    global lives
    lives
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
            lives = lives - 1
            incorrect_guess_letters = incorrect_guess_letters + guess

            if len(incorrect_guess_letters) == 7:
                display_current_game_status(incorrect_guess_letters, correct_letters, word)
                print("You are out of lives!\nAfter " + str(len(incorrect_guess_letters)) + " missed guesses and " + str(len(correct_letters)) + " correct guesses, the word was '" + word + "'")
                is_game_over = True

        if is_game_over:
            ask_to_play_again()







   