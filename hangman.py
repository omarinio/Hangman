import random
import string
import copy

# Picks random word from file
word_to_guess = random.choice(open("words.txt").read().split())
# Length of word to determine when game is over
word_length = len(word_to_guess)
# Number of guesses user had
num_of_guesses = 6
# Turns the word into a list of characters
word_array = list(word_to_guess)
guessing_array = []
used_letters = []


def setup():
    # Fills guessing array with empty placeholders
    for i in word_array:
        guessing_array.append('_')

    print(guessing_array)


def guess(letter):
    global word_length
    global used_letters
    global num_of_guesses

    prev_length = copy.deepcopy(word_length)
    for i, j in enumerate(word_array):
        if j == letter:
            guessing_array[i] = letter
            word_length = word_length - 1

    if prev_length == word_length:
        print("This letter does not match!\n")
        num_of_guesses = num_of_guesses-1

    used_letters.append(letter)
    print("You have used these letters: " + str(used_letters) + "\n")
    print("Number of guesses left: " + str(num_of_guesses) + '\n')
    print(guessing_array)


def user_input():
    global used_letters

    while num_of_guesses > 0 and word_length > 0:
        while True:
            user_input = input('Guess a letter: ')
            if len(user_input) == 1:
                if user_input in string.ascii_letters:
                    break
                print('Please enter only letters\n')
            else:
                print('Please enter only one character\n')
        guess_in_lower = user_input.lower()
        if guess_in_lower in used_letters:
            print("This letter has already been used!\n")
        else:
            guess(guess_in_lower)


def endgame():
    global num_of_guesses
    global word_to_guess

    if num_of_guesses == 0:
        print("You are out of guesses, you lose.\n")
        print("The word was: " + word_to_guess)
    else:
        print("You have guessed the word!\n")
        print("The word was: " + word_to_guess)


def main():
    setup()
    user_input()
    endgame()


main()
