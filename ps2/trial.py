# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 09:58:36 2018

@author: Magy Gamal
"""

import string
import random
WORDLIST_FILENAME = "words.txt"
def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word_guessed(secret_word,letters_guessed):
    x=None
    for letter in secret_word:
        if letter not in letters_guessed:
            x=False
            break
        else:  
            x=True
    return (x)

def get_guessed_word(secret_word,letters_guessed):
    x=""
    for letter in secret_word:
        if letter not in letters_guessed:
            x=x+"_ "
        else:
            x=x+letter
    return (x)

def get_available_letters(letters_guessed):
    x=""
    for letter in "abcdefghijklmnopqrstuvwxyz":
        if letter not in letters_guessed:
            x=x+letter
    return (x)

def match_with_gaps(my_word,other_word):
    my_word=my_word.replace(" ","")
    if len(my_word)!=len(other_word):
        return False
    for i in range(0,len(my_word)):
        if my_word[i]==other_word[i] or my_word[i]=="_":
            pass
        else:
            return False
    return True
def show_possible_matches(my_word):
    for word in wordlist:
        if match_with_gaps(my_word,word)==True:
            print(word)
wordlist= load_words()
secret_word = random.choice(wordlist)
    
def hangman(secret_word):
    guesses=6
    warnings=3
    letters_guessed=""
    print("Welcome to HANGMAN!")
    print("I am thinking of a word that is"+str(len(secret_word))+"long")
    print("_ "*len(secret_word))
    print("------------")
    while 1:
        letters=[]
        if guesses>0:
            print("Number of guesses left =" ,guesses )
            print("Number of warnings left=",warnings)
            print("Letters available:" + get_available_letters(letters_guessed))
            guess=input("Please enter a letter:")
            letters.append(guess)
            if guess == "*":
                guessed_word = get_guessed_word(secret_word, letters_guessed)
                show_possible_matches(guessed_word)
            if str.isalpha(guess):
                guess=str.lower(guess)
            else:
                print("That's not a letter,Please enter a letter:")
                warnings-=1
                if warnings<1:
                    guesses-=1
                continue
            if guess in letters_guessed:
                print("This letter has been guessed before")
                if warnings>0:
                    warnings-=1
                else:
                    guesses-=1
            letters_guessed=letters_guessed+guess
            if guess in secret_word:
                print("RIGHT")
            else:
                print("Ops that letter is not in my word")
                if guess in letters:
                    warnings-=1
                elif guess in ["a","o","i","e","u"]:
                    guesses-=2
                else:
                    guesses-=1
            print(get_guessed_word(secret_word,letters_guessed))
            if is_word_guessed(secret_word,letters_guessed):
                print("Congrations you have won")
                score=0
                unique=[]
                for letter in secret_word:
                    if letter not in unique:
                        unique.append(letter)
                score=guesses*len(unique)
                print("Score is",str(score))
                break
        else:
            print("Lost")
            print("The secret word was",secret_word)
            break
hangman(secret_word)
