# Name:
# Date:


# proj06: Hangman

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!
def hangman():
    winfactor=0
    listc=[]
    wronglist=[]
    alphalist= ["a","b","c", "d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    print "Welcome to hangman"
    #word=choose_word(wordlist)
    word = list(choose_word(wordlist))
    print word
    num_guess=len(word)
    length=len(word)
    LIST = [len(word) * "_ "]  #####
    print "The word is", length,"letters long. You have", length, "guesses."
    # for x in range(0,int(length)):
    #             listc.append("_ ")
    while num_guess!=0:
                print ""
                guess = raw_input("Guess a letter: ")
                print ""
                if guess in alphalist:
                    if guess in word:
                        print guess,"is in this word."
                        listc.append(guess)

                       #WHERE THE LETTER IS LOCATED, CODE  (INC)
                        # if guess==word[0]:
                        #     print ""
                        #     print guess,"is the first letter."
                        #     print ""
                        # if guess==word[int(length)-1]:
                        #     print ""
                        #     print guess,"is the last letter."
                        #     print ""

                    elif guess in listc:
                        print "You already guessed this. Please guess again."
                    elif guess in wronglist:
                        print "You already guessed this. Please guess again"
                    else:
                        print guess, "was not correct."
                        wronglist.append(guess)
                        num_guess=num_guess-1
                else:
                    print "Your guess was either capitalized, more than one letter, or it is not in the alphabet. Guess again."
                    print ""
                if num_guess==0:
                    print ""
                    print "YOU RAN OUT OF GUESSES"
                    print" "
                    print "The correct word was", word
                    print ""
                    print"--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
                    break
                print "wrong letters=", wronglist
                print""
                print "correct letters=", listc
                print ""
                print "You have", num_guess, "guesses left."
                if listc==word:
                    print"  Y"
                    print"      O"
                    print"          U"
                    print"  W"
                    print"      O"
                    print"          N"
                    print"--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
                    break


hangman()
#
# print word  #
# if guess in word:  #
#     if guess == word[0]:  #
#         LIST = [guess] + ((length - 1) * "_ ")  #
#         print LIST  #
#     else:  #
#         print LIST  #
# playagain= raw_input("Want to play again?(y or n)")
#
# if playagain==y:
#     hangman()
# else:
#     break
