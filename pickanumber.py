#pick a number
import re

count = 0
# randomly shuffle a sequence
from random import seed
from random import shuffle
# seed random number generator
seed(1)
# prepare a sequence
sequence = [i for i in range(100)]
# randomly shuffle the sequence
shuffle(sequence)
#print(sequence)
q = input('Enter a number ')
if q == 'quit' :
    print('Thanks for playing')
    quit()
Q = int(q)
a = (sequence[Q])
x = int(a)

while True :
    i = input( 'Whats your guess? ')
    if i == 'quit' :
        print('Thanks for playing')
        quit()
    try :
        int(i)
    except :
        print('Not a number')
        continue
    g = int(i)
    if g < x :
        print('Higher')
        print('Try again ')
    elif g > x :
        print('Lower')
        print('Try again ')
    elif g == x :
        print('Good job ')
        print(' . .')
        print('  U')
        print('Play again? ')
        c = input( 'y or n ')
        if c == 'y' :
            count = count + 1
            from random import seed
            from random import shuffle
            # seed random number generator
            seed(count)
            # prepare a sequence
            sequence = [i for i in range(100)]
            # randomly shuffle the sequence
            shuffle(sequence)
            shuffle(sequence)
            #print(sequence)
            q = input('Enter a number ')
            if q == 'quit' :
                print('Thanks for playing')
                quit()
            Q = int(q)
            a = (sequence[Q])
            x = int(a)
        elif c == 'n' :
            print('Thanks for playing')
            quit()
