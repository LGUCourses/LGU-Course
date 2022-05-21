#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random

n, odd = 0, 0 # ball number, odd identifier
result = ["Balanced", "Left pan is down", "Right pan is down"] # scale result

def introduction():
    # Introduction about 'Odd ball' game.
    print('-----------------------------------------------')
    print('  Welcome to the odd-ball game! You are given  ')
    print('  an even number of labelled balls, and among  ')
    print('  the balls one is heavier than the rest,      ')
    print('  called the odd ball.                         ')
    print('                                               ')
    print('  You are given a weighing scale and Your goal ')
    print('  is to find out which ball is the odd one.    ')
    print('                                               ')
    print('  Good Luck and have fun!                      ')
    print('-----------------------------------------------\n')


def congratulations():
    # Congratulations on the end of the game.
    print('/////////////////////////////////////////////')
    print('//                                         //')
    print('//    +   +                                //')
    print('//   +++ +++                               //')
    print('//  +++++++++                              //')
    print('//    +++++            /\                 ///')
    print('//     +++            /  \               / //')
    print('//      +            /    \             /  //')
    print('//                  /      \           /   //')
    print('//                 /        \_________/    //')
    print('//                /                        //')
    print('//               /       \         /       //')
    print('//              /       __\       /__      //')
    print('//             /                           //')
    print('//            /             ____           //')
    print('//           /              \  /           //')
    print('//          /     _~_        \/    _~_     //')
    print('//         /     /  /             |   |    //')
    print('//        /     /  /              |   |    //')
    print('//       /     /  /               |   |    //')
    print('/////////////////////////////////////////////')


def get_ball_number() -> int:
    # Check that the user enter a even number of balls.
    while True:
        n = input('Enter a even number of balls to begin the game: ')
        try:
            n = eval(n)
            if n > 0 and n % 2 == 0:
                print('Alright! The game will begin with {} balls.\n'.format(n))
                break
                # Obtain the valid ball number and finish.
            else:
                print('Please try again! Notice that the number must be even.')
        except:
            print('Please try again! Notice that the number must be even.')
            # Re-input if the number is invalid.
    
    return n


def user_scale_operation():
    # Interaction part of scale.
    print('You are prompt to enter the balls to be placed on the pans of scale,')
    print('seperate each ball identifier with at least one minimum space, e.g. 1 2 3')

    while True:
        left_input = input('Enter the identifier(s) to be placed on left pan: ')
        right_input = input('Enter the identifier(s) to be placed on right pan: ')

        left = left_input.split()
        right = right_input.split()
        valid = True                      # Marks the validity of the input.
        vis = {}                          # Checking for duplicate elements.
           
        # The two sides of scale are inequal.
        if len(left) != len(right) or len(left) == 0:
            valid = False

        total = left + right
        # Three invalid cases: illegal character or duplicated or out of range.
        for num in total:
            if (not num.isdigit()) or vis.get(num, 0) or (int(num)<1 or int(num)>n):
                valid = False
            vis[num] = 1

        if valid == True:
            # Marks the odd ball.
            odd_pos = 0
            for num in left:
                if int(num) == odd:
                    odd_pos = 1
            for num in right:
                if int(num) == odd:
                    odd_pos = 2
            print('The scale shows: {}.'.format(result[odd_pos]))
            break
        else:
            print('Your inputs for left: \"{}\", right: \"{}\"\n'.format(left_input, right_input))
            print('Invalid input!\n')
            print('Please ensure correct ball identifiers (1-{}) are entered on each pan, '.format(n))
            print('no duplicate balls on either or both pans. Both pands should have the')
            print('same number of balls and must have at least one ball.')
            # Error
            
    return


def user_guess_number():
    # Interaction part of guessing number.
    opt = input('Enter the odd ball number or Enter any other keys to weigh again: ')
    if not opt.isdigit():
        return None
    
    return int(opt)


def play():
    # Start the game.
    global n, odd
    n = get_ball_number()
    odd = random.randint(1, n)
    # print('The answer is: {}'.format(odd))

    # The main process.
    count_scale = 0
    count_guess = 0

    while True:
        count_scale += 1
        user_scale_operation()
        num = user_guess_number()

        if num == None:
            continue
            
        count_guess += 1
        if odd != num:
            print('Sorry, your answer is not correct!\n\n')
        else:
            print('---------------------------------------------')
            print('  Conguratulations! Your answer is correct!  ')
            print('         Total scale usage count: {}         '.format(count_scale))
            print('         Total guess uasga count: {}         '.format(count_guess))
            congratulations()
            break

    return


if __name__ == "__main__":
    introduction()
    while True:
        play()
        opt = input('\nWanna play again? (y/n) ')
        if opt != 'y':
            break
