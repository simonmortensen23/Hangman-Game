# Hangman - Rite of Words and Life
Hangman - Rite of Words and Life is a Python terminal game, which runs in the Code Institute mock terminal on Heroku. 
The main goal of this game is for the user to guess a random word that the computer chooses by guessing one letter at the time. This project was inspired by the blackboard game you played while in primary school and is suited for one or more players.
The games origins is not totally clear, although author and word game expert Tony Augarde notes the the game may have emerged in the victorian times according to [Ludozofi](https://www.ludozofi.com/home/games/hangman/). 

## How To Play
Hangman - Rite of words and Life is based on the classic paper / blackboard game.

The player has to enter their name and the game will start.

The computer will choose a random word from the list of words, that the player has to guess.

The player has seven tries to guess the word and win the game.

## Features
### Existing Features
- Welcome message
  - Player asked to enter name
![Welcome](https://user-images.githubusercontent.com/43667190/159117058-a93a00d5-81fb-4bb2-a515-8e8c8188da68.PNG)
- Random word is chosen and hidden under the underscores
![1st](https://user-images.githubusercontent.com/43667190/159117157-d6b1fa97-6345-4d27-8c05-c2cb2e775ab9.PNG)
- Player input accepted
- Stores wrong guessed letters for the player to see
![2nd](https://user-images.githubusercontent.com/43667190/159117188-e6ee3b32-769f-40e3-882b-e9ece59428b5.PNG)


### Future Features
- Allow the player to choose difficulty
- Scoreboard and points system
- Add your own words to the list 
## Data Model

## Testing
I have manually tested this project by following:
- Passed the code through a PEP8 linter and confirmed there are no problems
- Given invalid inputs: numbers when strings are expected, same input twice, multiple letters when one is expected
- Tested in my local terminal and the Code Institute Heroku terminal

### Bugs
### Solved Bugs
- When I first deployed the project to heroku I got an error "ModuleNotFoundError: No module named colorama". I fixed it by adding the right information to requirments.txt for heroku to read installed modules.

### Remaining Bugs
- No bugs remaining.

### Validator Testing
- PEP8
  - No errors were returned from [PEP8online.com](http://pep8online.com/checkresult)
## Deployment

## Credits
