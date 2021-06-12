import random
from words import words
import string


def get_valid(words):
    word = random.choice(words)
    while "-" in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = get_valid(words)
    letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # to keep track of users guesses

    lives = 6
    print("------------HANGMAN GAME-------------")
    while len(letters) > 0 and lives > 0:
        print("You have", lives, "lives left and used these letters: ", ' '.join(used_letters))
        #  what their current word is
        words_list = [let if let in used_letters else '_' for let in word]
        print("Current Word: ", ' '.join(words_list))
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word:
                letters.remove(user_letter)
            else:
                lives = lives - 1
                print("Letter is not in the word.")
        elif user_letter in used_letters:
            print("Already used, Please try again!")
        else:
            print("Invalid Character!")
    if lives == 0:
        print("Sorry you have died, the word was:", word)
    else:
        print("Yayy!! You have won")
        print("You have guessed the word: ", word, "!!")


hangman()
