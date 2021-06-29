#!/usr/bin/python3
from math import trunc
import random

def whatsTheWord():
    name = str(input("Enter Your Name: "))
    print("Good Luck: ",name)
    words = ['rainbow', 'computer', 'science', 'programming','python', 'mathematics', 'player', 'condition','reverse', 'water', 'board', 'geeks']
    word = random.choice(words)
    print("Guess the characters....")
    guesses = ''
    turns = 12
    failds = 0
    while turns > 0:
        if word:
            for char in word:
                if char in guesses:
                    print(char)
                else:
                    print(" ")
                    failds +=1
        guess = input("guess the charactor: ")
        guesses += guess
        turns -= 1
        print("Wrong..")
        print("You have", + turns, 'more guesses')
        if turns == 0:
            print("You Loose...")
        if failds == 0:
            print("You Win..")
            print("The word is: ",word)
            break


whatsTheWord()