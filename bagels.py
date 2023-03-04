'''Deductive logic game by Al Sweigart. You'll have to use clues to figure out the correct number.'''

import random
NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    print ('''I am thinking of a {}-digit numbers that does not repeat digits. You will be given clues based on three key words.
    Pico: One digit is correct, but it is not in the correct position.
    Fermi: One digit is both correct and in the correct position.
    Bagels: No digit is correct.'''.format(NUM_DIGITS))

    while True: # This is the main game loop
        # This will be a secret number that the user has to guess
        secretNum = getSecretNum()
        print('I thought of a number!')
        print('You have {} guesses.'.format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            # This while loop will have the user guess until they enter something valid
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}. '.format(numGuesses))
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break # This means that the user has guessed the correct number
            if numGuesses > MAX_GUESSES:
                # Loop until answer is provided (Game Loss)
                print('You are out of guesses!')
                print('The answer was {}. '.format(secretNum))
            
        print('Would you like to play again? (Yes or No)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing Bagels!')

def getSecretNum():
    numbers = list('0123456789')
    random.shuffle(numbers)

    secretNum = ' '
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    if guess == secretNum:
        print('Correct!')

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi') 
        elif guess[i] in secretNum:
            clues.append('Pico')
        if len(clues) == 0:
            return 'Bagels'
        else:
            clues.sort() # <-- This function will sort the clues in an alphabetical fashion
            return ' '.join(clues) # <-- Single string from the list of string clues
        
if __name__ == '__main__':
    main()

