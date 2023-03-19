import random

print("Welcome to Hangman!!!")

word_dictionary = ['horse', 'snake', 'giraffe', 'elephant', 'tiger', 'squirrel', 'antelope', 'kangaroo']
#choose a random word
randomWord = random.choice(word_dictionary)

for x in randomWord:
    print("-", end="")
def print_hangman(wrong):
    if wrong == 0:
        print("\n +----+")
        print("        |")
        print("        |")
        print("        |")
        print("    =====")
    elif wrong == 1:
        print("\n +----+")
        print(" O    |")
        print("      |")
        print("      |")
        print(" =====")
    elif wrong == 2:
        print("\n +----+")
        print(" O    |")
        print(" |    |")
        print("      |")
        print("  =====")
    elif wrong == 3:
        print("\n +----+")
        print(" O    |")
        print("/|    |")
        print("      |")
        print("  =====")
    elif wrong == 4:
        print("\n +----+")
        print(" O    |")
        print("/|\   |")
        print("      |")
        print("  =====")
    elif wrong == 5:
        print("\n +----+")
        print(" O    |")
        print("/|\   |")
        print("/|    |")
        print("  =====")
    elif wrong == 6:
        print("\n +----+")
        print(" O    |")
        print("/|\   |")
        print("/|\   |")
        print("  =====")

def printWord(guessedLetters):
    counter = 0
    rightLetters = 0
    for char in randomWord:
        if char in guessedLetters:
            print(randomWord[counter], end="")
            rightLetters += 1
        else:
            print(" ", end="")
        counter += 1
    return rightLetters

length_of_guess_word = len(randomWord)
amount_of_wrong_try = 0
current_guess_index = 0
current_letters_guess = []
current_right_letters = 0
while (amount_of_wrong_try != 6 and length_of_guess_word != current_right_letters):
    print("\nLetters guessed so far: ")
    for letters in current_letters_guess:
        print(letters, end="")
    lettersGuessed = input("\nPlease guess the letter: ")
    if randomWord[current_guess_index] == lettersGuessed:
        print_hangman(amount_of_wrong_try)
        current_guess_index += 1
        current_letters_guess.append(lettersGuessed)
        current_right_letters = printWord(current_letters_guess)
        print()
    else:
        amount_of_wrong_try += 1
        current_letters_guess.append(lettersGuessed)
        print_hangman(amount_of_wrong_try)
        current_right_letters = printWord(current_letters_guess)
        print()

print("Thank you for playing! See you next time :)")