# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random



lives = "hangman"
words = ["orangutan", "message", "breakfast"]

def getWord(wordList):
    """
    This function selects and returns a random word from the words.py file
    """
    word = random.choice(words) #Chooses random word from words array
    return word

def displayGame(missedLetters, correctLetters, unknownWord):
    """
    This function prints the layout of the playerboard and updates it after every turn
    """
    playerLives = '_' * len(lives)
    print(playerLives)
    
    print(f"Player: {playerName} from {playerCity}")
    print()
    print(f"Letters you have guessed wrong so far: ", ' '.join(missedLetters))
    print()
    blanks = '_' * len(unknownWord) #Finds _ * the length of the unknown word
    
    for i in range(len(unknownWord)):
        if unknownWord[i] in correctLetters:
            blanks = blanks[:i] + unknownWord[i] + blanks[i+1:]
    
    for letter in blanks:
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

def playAgain():
    """
    This function asks the player if they want to play again or quit the game
    """
    play_again = input("Do you want to play again? (yes or no): ")
    if play_again == "yes":
        gameOver = False
    else:
        print("Game is over, enjoy your day!")


print("HANGMAN") 
missedLetters = ''
correctLetters = ''
unknownWord = getWord(words)
gameOver = False
playerName = input("Enter your name: ")
print()
playerCity = input("Enter your city: ")
print()


while True:
    displayGame(missedLetters, correctLetters, unknownWord)

    guess = playerGuess(missedLetters + correctLetters)
    
    
    if guess in unknownWord:
        correctLetters = correctLetters + guess

        foundAllLetters = True
        for i in range (len(unknownWord)):
            if unknownWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print("Congratiulations! You have guessed the word: " + unknownWord)
            gameOver = True
    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(lives):
            displayGame(missedLetters, correctLetters, unknownWord)
            print("You are out of lives!\nAfter " + str(len(missedLetters)) + " missed guesses and " + str(len(correctLetters)) + " correct guesses, the word was '" + unknownWord + "'") 
            gameOver = True

    if gameOver:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameOver = False
            secretWord = getRandomWord(words)
        else:
            break






   