# import modules
import random
import time

# define variables
wordList = ['asshole', 'poop', 'abyss', 'amongus', 'devil', 'pipe', 'awkward', 'bagpipes', 'bandwagon', 'beekeeper', 'gnarly', 'gossip', 'grogginess', 'haiku', 'haphazard', 'hyphen', 'icebox', 'injury', 'ivy', 'jackpot', 'jockey', 'jogging', 'joking', 'jovial', 'joyful', 'juicy', 'jukebox', 'jumbo', 'kayak', 'kazoo', 'uptown', 'vaporize', 'shrek', 'vodka', 'voodoo', 'vortex', 'waxy', 'wellspring', 'wheezy', 'whiskey', 'whizzing', 'whomever', 'wimpy', 'witchcraft', 'wizard', 'woozy', 'wristwatch', 'wyvern', 'xylophone', 'yachtsman', 'underwear', 'somebody', 'tasty', 'yummy', 'zephyr', 'zigzag', 'evil', 'enemie', 'zipper', 'zodiac', 'zombie']
word = random.choice(wordList)
guess = ''
guessList = []
guessCount = 0

# define functions
def print_hangman(guessCount):
    if guessCount == 0:
        print('_________')
        print('|       |')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
    elif guessCount == 1:
        print('_________')
        print('|       |')
        print('|       O')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
    elif guessCount == 2:
        print('_________')
        print('|       |')
        print('|       O')
        print('|       |')
        print('|')
        print('|')
        print('|')
        print('|')
    elif guessCount == 3:
        print('_________')
        print('|       |')
        print('|       O')
        print('|      /|')
        print('|')
        print('|')
        print('|')
        print('|')
    elif guessCount == 4:
        print('_________')
        print('|       |')
        print('|       O')
        print('|      /|\\')
        print('|')
        print('|')
        print('|')
        print('|')
    elif guessCount == 5:
        print('_________')
        print('|       |')
        print('|       O')
        print('|      /|\\')
        print('|      /')
        print('|')
        print('|')
        print('|')
    elif guessCount == 6:
        print('_________')
        print('|       |')
        print('|       O')
        print('|      /|\\')
        print('|      / \\')
        print('|')
        print('|')
        print('|')

# main program
print('Welcome to Hangman!')
print('The word has', len(word), 'letters')
print('You have 6 guesses')
print('Good luck!')
print('Created by tomotow!')

# loop until the word is guessed
while guess != word:
    # get a guess from the user
    guess = input('Guess a letter: ')
    guess = guess.lower()

    # check if the guess is valid
    if len(guess) != 1:
        print('You can only guess a single letter!')
    elif guess in guessList:
        print('You already guessed the letter', guess)
    elif guess not in 'abcdefghijklmnopqrstuvwxyz':
        print('You can only guess letters!')
    else:
        # check if the guess is correct
        if guess in word:
            print('Good job!', guess, 'is in the word')
        else:
            print('Sorry', guess, 'is not in the word')
            guessList.append(guess)
            guessCount += 1

    # print the hangman
    print_hangman(guessCount)

    # check if the user has guessed too many times
    if guessCount == 6:
        print('Sorry, you ran out of guesses. The word was', word)
        break

    # check if the user has guessed the word
    if guess == word:
        print('Congratulations, you guessed the word!')
        print('You guessed the word in', guessCount, 'guesses')
        print('The word was', word)

# check if the user has entered an invalid response
else:
    print('Invalid response!')