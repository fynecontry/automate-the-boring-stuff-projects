#!/usr/bin/env python3
import random

def flip_generator(coin):
    '''flips a coin 100 times to randomly generate  heads or tails'''
    for i in range(100):
        # 0 for heads 1 for tails
        if random.randint(0, 1) == 0:
            coin.append('H')
        else:
            coin.append('T')



def check_streak(coin):
    '''checks the number of 6 streaks of H/T'''
    streak_counter = 0
    number_of_streaks = 0
    for index in range(1, len(coin)):
        # increase sequence if current value matches previous.
        if coin[index] == coin[index - 1] and streak_counter < 6:
            streak_counter += 1
        else:
            streak_counter = 0      # reset streak_counter if no streak
        # store 6 matching sequence as a streak
        if streak_counter == 6:
            number_of_streaks += 1

    return number_of_streaks
    
if __name__ == "__main__":
    number_of_streaks = 0

    for experiment_number in range(10000):
        # Create a list of 100 'heads' or 'tails' values.
        coin = []
        flip_generator(coin)
        
        # Get # of streak of 6 heads or tails in a row
        number_of_streaks += check_streak(coin)

    # Display % of streaks
    print('Chance of streak: %s%%' % (number_of_streaks/100))



