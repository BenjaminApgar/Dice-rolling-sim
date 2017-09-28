# This program is designed to simulate any kind and any amount of dice.

def diceNum():
    ''' 
        gets the number of dice to be rolled
    '''
    while True:
        try:
            compset = int(input("Enter the amount of dice you want to roll: "))

            if compset <= 0:
                raise ValueError
            break
        except ValueError:
            print("it didn't work")
    return compset

def diceSides():
    ''' 
        gets the number of sides on the dice
    '''
    while True:
        try:
            compset = int(input("Enter the amount of sides the dice have: "))
            break
        except ValueError:
            print("That's not a valid input")
    return compset

def modeSelect():
    '''
        prompts the user to select a mode of display and handles error checking
    '''
    mode = ' '
    while mode != "s" or mode != "s":
        mode = input("Enter your mode ('s' for sum 'i' for individual): ",)
        if mode == "i":
            return mode
        elif mode == "s":
            return mode
        else: mode = " "

def zeroSelect():
    zero = ' '
    while zero != "y" or zero != "n":
        zero = input("Do you want to include zero? (y/n): ",)
        if zero == "n":
            return zero
        elif zero == "y":
            return zero
        else: zero = " "

def noZeroMode(mode):
    '''
        Rolls the dice and handles quitting, acts as a realistic dice
    '''
    if mode == "i":

        finish = 0
        while finish != num:
            print("roll ", finish + 1 , " is ", random.randint(1, sides))
            finish += 1
        answer = ''
        while answer != 'n' and answer != 'y':
            answer = input("Do you want to roll again? (y/n): ")
        if answer == 'n':
            return 'quit'
    elif mode == "s":
        finish = 0
        summed = 0
        while finish != num:
            summed += random.randint(1, sides)
            finish += 1
        print("the sum of ", num, " roles of a ", sides, " sided dice is: ", summed)
        answer = ''
        while answer != 'n' and answer != 'y':
            answer = input("Do you want to roll again? (y/n): ")
        if answer == 'n':
            return 'quit'

def zeroMode(mode):
    '''
        The exact same code as noZeroMode, but includes a 0 as a possible side
        of the dice, useful for 4chan id rolls and similer games
    '''
    if mode == "i":

        finish = 0
        while finish != num:
            print("roll ", finish + 1 , " is ", random.randint(0, sides))
            finish += 1
        answer = ''
        while answer != 'n' and answer != 'y':
            answer = input("Do you want to roll again? (y/n): ")
        if answer == 'n':
            return 'quit'
    elif mode == "s":
        finish = 0
        summed = 0
        while finish != num:
            summed += random.randint(0, sides)
            finish += 1
        print("the sum of ", num, " roles of a ", sides, " sided dice is: ", summed)
        answer = ''
        while answer != 'n' and answer != 'y':
            answer = input("Do you want to roll again? (y/n): ")
        if answer == 'n':
            return 'quit'

def runFunction(mode, zero):
    '''
        runs either the zero or no zero functions and quits the program
    '''
    quit_check = ''
    if zero == 'y':
        quit_check = zeroMode(mode)
        if quit_check == 'quit':
            return 'quit'
    if zero == 'n':
        quit_check = noZeroMode(mode)
        if quit_check == 'quit':
            return 'quit'


    

# main ------------------------------------------------------------------------
import random

print("welcome to Ben's dice simulator!" )
quit = False
while not quit:
    num = diceNum()
    sides = diceSides()
    zero = zeroSelect()
    mode = modeSelect()
    quit_detect = runFunction(mode, zero)
    if quit_detect == 'quit':
        quit = True
print("Goodbye, come again soon!")
