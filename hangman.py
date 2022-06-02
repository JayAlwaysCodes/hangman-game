# from lib2to3.pytree import LeafPattern
# import random
# from words import words
# import string

# def get_valid_word(word):
#     word = random.choice(words) #randomly chooses something from the list
#     while '-' in word or ' ' in word:
#         word = random.choice(words)
#     return word

# def hangman():
#     word = get_valid_word(words)
#     word_letters = set(word)  #letters in the word
#     alphabet = set(string.ascii_uppercase)
#     used_letters = set()  #what the user has guesed

#     lives = 6

#     #getting user input
#     while len(word_letters) > 0 and lives > 0:
#         #letters used
#         print ('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

#         #what current word is (ie W - R D)
#         letter = [letter if letter in used_letters else '-' for  letter in word]
#         print('current word: ', ' '.join(letter))



#         user_letter = input('Guess a letter: ').upper()
#         if user_letter in alphabet - used_letters:
#             used_letters.add(user_letter)
#             if user_letter in word_letters:
#                 word_letters.remove(user_letter)
#             else:
#                 lives = lives - 1 #takes away life if wrong
#                 print('Letter is not in the word')
#         elif user_letter in used_letters:
#             print('You have already used that character, please try again')
#         else:
#             print('Invalid Character, Please try again')

#     if lives == 0:
#         print("sorry, you died, The word was: ",word)
#     else:

#         print("You guessed the word", word,"!!")


# hangman()


from itertools import count
from operator import length_hint
import random

import time

#initial steps to invite in the game:
print("\n Welcomme to Hangman game")
name = input("Enter your name: ")
print("Hello "+ name + " Best of luck!!")
time.sleep(2)
print("The game is about to Start!\nLet's play Hangman!")
time.sleep(3)

#The parameters we require to execute the game:
def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = ['january','border','image','film','promise','kids','lungs','doll','rhyme','damage','plants']
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '_'*length
    already_guessed = []
    play_game = ''

#A loop to re-excute the game when the first round ends

def play_loop():
    global play_game
    play_game = input("Do You want to play again? y=Yes, n=No \n").lower()
    while play_game not in ['y', 'n']:
        play_game = input("Do You want to play again? y=Yes, n=No \n").lower()
    if play_game == 'y':
        main()
    elif play_game == 'n':
        print("Thanks for playing, We expect you back again!")
        exit()
#Initializing all the conditions required for the game
def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 6
    guess = input("This is the hangman word: "+ display +" Enter your guess word: \n")

    guess = guess.strip()
    if len (guess.strip()) == 0 or len(guess.strip()) >=2 or guess <= '9':
        print("Invalid Input, Try a letter\n")
        hangman()
    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word [index + 1:]
        display = display[:index] + guess + display [index + 1:]
        print(display + '\n')
    elif guess in already_guessed:
        print("Try another Letter. \n")
    
    else:

        count += 1

        if count == 1:
            time.sleep(1)
            print(" |   \n"
                  " |   \n"
                  " |   \n"
                  " |   \n"
                  " |   \n"
                  "_|_ \n")
            print("Wrong guess. " + str(limit - count)+ " guess remaining\n")
        elif count == 2:
            time.sleep(1)
            print(" ____  \n"
                  " |     \n"
                  " |     \n"
                  " |     \n"
                  " |     \n"
                  " |     \n"
                  "_|_    \n")
            print("Wrong guess. " + str(limit - count)+ " guess remaining\n")
        elif count == 3:
            time.sleep(1)
            print("  ____  \n"
                  " |    |  \n"
                  " |     \n"
                  " |     \n"
                  " |     \n"
                  " |     \n"
                  "_|_    \n")
            print("Wrong guess. " + str(limit - count)+ " guess remaining\n")
        elif count == 4:
            time.sleep(1)
            print("  ____  \n"
                  " |    |  \n"
                  " |    | \n"
                  " |     \n"
                  " |     \n"
                  " |     \n"
                  "_|_    \n")
            print("Wrong guess. " + str(limit - count)+ " guess remaining\n")
        elif count == 5:
            time.sleep(1)
            print("  ____  \n"
                  " |    |  \n"
                  " |    | \n"
                  " |    o \n"
                  " |     \n"
                  " |     \n"
                  "_|_    \n")
            print("Wrong guess. " + str(limit - count)+ " guess remaining\n")
        elif count == 6:
            time.sleep(1)
            print("  ____  \n"
                  " |    |  \n"
                  " |    |  \n"
                  " |    o  \n"
                  " |   /|\ \n"
                  " |   / \ \n"
                  "_|_      \n")
            print("Wrong guess. You are hanged!!! \U0001F923- \n")
            print("The word was: ", already_guessed, word)
            play_loop()
    if word == "_" * length:
        print("Congrats! You have guessed the word correctly! \U0001f600")
        play_loop()
    elif count != limit:
        hangman()
main()
hangman()
