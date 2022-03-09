# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
from words import words

def getWord(wordList):
    """
    This function selects and returns a random word from the words.py file
    """
    wordIndex = random.randint(0, len(wordIndex) - 1)
    return wordList(wordIndex)


def newGame():
    print("HANGMAN") 
    missedLetters = ''
    correctLetters = ''
    unknownWord = getWord(words)
    gameOver = False

    

#def getRandomWord():

#def playerInput():

#def checkPlayerInput():

#def addScore():

#def playAgain():

#def endGame():

newGame()


   