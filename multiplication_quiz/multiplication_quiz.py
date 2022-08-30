#!/usr/bin/env python3

import pyinputplus as pyip
import time, random

number_of_questions = 10
correct_answers = 0

for question in range(number_of_questions):
    # Get 2 random numbers between 0 - 9
    num1 = random.randint(0, 9)
    time.sleep(0.5)
    num2 = random.randint(0, 9)

    try:
        # allowRegexes check input matches answer, blockRegexes flag incorrect answers
        pyip.inputStr(prompt=f'{num1} x {num2}: ', timeout=8, limit=3, 
                allowRegexes=['^%s$'%(num1 * num2)], blockRegexes=[('.*', 'Incorrect!')])

    except pyip.TimeoutException:
        if question < 9:
            print('Timeout, moving on to next question')
            continue
        else:
            print('Timeout, calculating result...')

    except pyip.RetryLimitException:
        if question < 9:
            print('Out of tries!, moving on to next question')
            continue
        else:
            print('Out of tries, calculating result...')

    else:
        print('Correct!')
        correct_answers += 1

print(f'You scored: {correct_answers}/{number_of_questions}')
