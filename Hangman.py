import random
import string

WORDLIST_FILENAME = "C:\Users\shivasathi\Desktop\words.txt"

def loadWords():
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    line = inFile.readline()
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    return random.choice(wordlist)
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    for c in secretWord:
        if(not(c in lettersGuessed)):
            return False
    return True

def getGuessedWord(secretWord, lettersGuessed):
    str=''
    for c in secretWord:
         if(not(c in lettersGuessed)):
             str+='_'
         else:
             str+=c
    return str

def getAvailableLetters(lettersGuessed):
    str='abcdefghijklmnopqrstuvwxyz'
    newStr=''
    for s in str:
        if(not(s in  lettersGuessed)):
            newStr+=s
    return newStr
    

def hangman(secretWord):
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is "+str(len(secretWord))+" letters long.")
    i=8
    lettersGuessed=[]
    while(i>0):
        print("-----------")
        print("You have "+str(i)+" guesses left.")
        print("Available letters:"+getAvailableLetters(lettersGuessed))
        letter=raw_input("Please guess a letter: ")
        letter=letter.lower()
        if(letter in lettersGuessed):
            print("Oops! You've already guessed that letter: "+getGuessedWord(secretWord, lettersGuessed))
        else:
            lettersGuessed+=letter 
            
            if(isWordGuessed(letter,secretWord)):
                print("Good guess: "+getGuessedWord(secretWord, lettersGuessed))
            else:
                print("Oops! That letter is not in my word:"+getGuessedWord(secretWord, lettersGuessed))
                i-=1
        
        if(secretWord==getGuessedWord(secretWord, lettersGuessed)):
            print("------------")
	    print("Congratulations, you won!")
	    break
    if(secretWord!=getGuessedWord(secretWord, lettersGuessed)):   
        print("------------")
        print("Sorry, you ran out of guesses. The word was "+secretWord)
    
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)