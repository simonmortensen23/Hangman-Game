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

- Input validation and error-checking
  - You can only enter one letter at the time
  - You must enter letters from the english alphabet
  - You cannot enter the same guess twice

![image](https://user-images.githubusercontent.com/43667190/159118388-e8371cec-bca0-46f4-a6f0-31b171a3c5a3.png)

### Future Features
- Allow the player to choose difficulty
- Scoreboard and points system
- Add your own words to the list 

### Games stages
- First stage after player enters username
  - Hangman stages
  - Underscores shows the length of the word
  - Letters guessed wrong
  - Letters guessed right
  - Input to guess a letter

![1st](https://user-images.githubusercontent.com/43667190/159118730-3bbf8afd-8f11-4fb9-8ca9-c64ffb79b124.PNG)

- Second stage
  - Whenever the player guesses a wrong letter, a new part of the hangman appears
  - Wrong letter is added to the list of wrong letters
  - After one wrong guess the head appers
  
![2nd](https://user-images.githubusercontent.com/43667190/159118928-c90d1236-50be-4ae2-b5a1-31f3bd7c784f.PNG)

- Stage 3
  - After two wrong guesses the neck appears

![3rd](https://user-images.githubusercontent.com/43667190/159118992-be6c51d6-8930-4814-9826-9cd5d16d0161.PNG)

- Stage 4
  - After three wrong guesses the right arm appears

![4th](https://user-images.githubusercontent.com/43667190/159119169-797da5f0-03ad-4f0c-ada9-734b82fb8bf0.PNG)

- Stage 5
  - After four wrong guesses the left arm appears

![5th](https://user-images.githubusercontent.com/43667190/159119181-6de34372-7b34-478b-a24a-678016474e06.PNG)

- Stage 6
  - After five wrong guesses the right leg appears

![6th](https://user-images.githubusercontent.com/43667190/159119184-3ec9aa3e-792e-4625-a687-78aa11b869bb.PNG)

- Stage 7
  - After six wrong guesses the left leg appears

![7yh](https://user-images.githubusercontent.com/43667190/159119189-8a8d50c8-265a-4074-9fae-4413be3ea43c.PNG)

- Stage 8
  - After seven wrong guesses the head will turn from "o" to "x" to show that the game is over

![final](https://user-images.githubusercontent.com/43667190/159119210-76cf2e22-be84-4d95-9c58-fe9cee3c3bd0.PNG)

- Win
  - If the player guesses all the correct letters in the random word the stickman will return safely to the ground

![win](https://user-images.githubusercontent.com/43667190/159119215-0bb187e4-d267-41a7-b087-760dda03f800.PNG)

- Play Again
  - Ask if player wants to play again using "yes" or "no" input

![newGameYes](https://user-images.githubusercontent.com/43667190/159119231-046dda07-7142-4586-9e71-e9422ac1c9ad.PNG)

- Goodbye
  - If player types "no" in play again the game will print a message and shut down

![goodbye](https://user-images.githubusercontent.com/43667190/159119238-d1bb23ba-1f26-47bb-ba84-304ff808c98f.PNG)

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
  - No errors were returned from PEP8online.com
  
## Deployment
This Project was deployed using Code Institute's mock terminal for Heroku.
- Step for deployment:
  - Fork or clone this repository
  - Create a new Heroku app
  - Set the buildsbacks to Python and NodeJS in that specific order
  - Link Heroku app to the repository
  - Click on Deploy
  
## Credits
- Code institute for the deployment terminal
- Chris Horton for the [Hangman art & wordslist](https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c) 
