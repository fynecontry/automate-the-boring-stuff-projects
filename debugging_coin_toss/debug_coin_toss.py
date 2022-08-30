#!/usr/bin/env python3

import random, logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s') 

logging.info('Start of game')

guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    guess = guess.lower()

toss = random.randint(0, 1) # 0 is tails, 1 is heads
if toss == 0:
    toss = 'tails'
else:
    toss = 'heads'

logging.debug(f'Value by user {guess} - Coin toss value {toss}')
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    logging.debug(f'Value by user {guess} - Coin toss value {toss}')
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')

logging.info('End of game')
