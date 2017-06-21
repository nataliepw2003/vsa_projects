# Name:
# Date:


""" 
proj 03: Guessing Game

Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, 
or exactly right. Keep the game going until the user types exit.
Keep track of how many guesses the user has taken, and when the game ends, print this out.

"""
import random
carrot=random.randint(1,9)
supercalifragilisticexpialidocious=raw_input("Name:")
print "Hi,",supercalifragilisticexpialidocious,"! Let's play a guessing game!"
starbucks= raw_input("Guess a number between 1 and 9."  )
if starbucks== "exit" or starbucks== "EXIT" or starbucks== "Exit":
    print "You have chosen to give up. The answer was",carrot
elif starbucks== "1" or starbucks== "2" or starbucks== "3" or starbucks== "0" or starbucks== "4" or starbucks== "5" or starbucks== "6" or starbucks== "7" or starbucks== "8" or starbucks== "9":
    starbucks=int(starbucks)
    if starbucks==carrot:
        print "Oh my goodness? How did you guess? You must be magic,",supercalifragilisticexpialidocious,"!"
        print "That only took one guess!"
    elif starbucks!=carrot:
        if starbucks > carrot:
            x = 0
            x = x + 1
            print "That answer was too big! Try again!"
        elif starbucks < carrot:
            x = 0
            x = x + 1
            print "That answer was too small! Try again!"
    else:
        print "That answer doesn't work. Please restart the program and try again."
    while starbucks!= carrot:
        if x==5:
            print "Sorry, you are out of guesses. The number was",carrot,"."
            break
        starbucks= raw_input("Guess another number (1-9). ")
        if starbucks=="exit":
            print "You have chosen to give up. The answer was", carrot,"."
        else:
            starbucks= int(starbucks)
            if starbucks == carrot:
                print "Good job,",supercalifragilisticexpialidocious,",you guessed the number in",x+1,"tries!"
            elif starbucks != carrot and x<5 and starbucks>0 and starbucks<10:
                x = x + 1
                if starbucks > carrot and x<5:
                    print "That answer was too big! Try again!"
                elif starbucks < carrot and x<5:
                    print "That answer was too small! Try again!"
            else:
                print "Please do not type anything other than a number in the range of 1-9. If you do type something else, you will make me very confused :("
                print "If you would like to continue, please run the program again."
else:
    print "Please do not type anything other than a number in the range of 1-9. If you do type something else, you will make me very confused :("
    print "If you would like to continue, please run the program again."

#make it so only numbers 1-9 can be typed in (not more or less)



