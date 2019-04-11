#!/usr/bin/env python
#python3

import random

def print_board(set1,set2,set3):
    #set1 is empty place list, set2 is 'O' list, set3 is 'X' list
    result=[]
    for i in range(1,10):
        if i in set1:
            result.append(' ')
        elif i in set2:
            result.append('O')
        elif i in set3:
            result.append('X')
    print(result[6]+'|'+result[7]+'|'+result[8])
    print('-+-+-')
    print(result[3]+'|'+result[4]+'|'+result[5])
    print('-+-+-')
    print(result[0]+'|'+result[1]+'|'+result[2])

def is_win(set1):
    if {1,2,3}.issubset(set1) or {4,5,6}.issubset(set1) \
            or {7,8,9}.issubset(set1) or {1,4,7}.issubset(set1) or {2,5,8}.issubset(set1) \
            or {3,6,9}.issubset(set1) or {1,5,9}.issubset(set1) or {3,5,7}.issubset(set1):
                return True
    else:
        return False

def AI_move(set1,set2,set3):
    # set1 is remaining place list, set2 is AI already placed list, set3 is my placed list
    flag=0
    for i in set1:
        if is_win(set2 | {i}):
            next_move=i
            flag=1
            break
    if flag==0:
        for i in set1:
            if is_win(set3 | {i}):
                next_move=i
                flag=1
                break
    if flag==0 and len({1,3,7,9} & set1)>0:
        next_move=random.choice(list({1,3,7,9} & set1))
        flag=1
    elif flag==0 and {5}.issubset(set1):
        next_move=5
        flag=1
    elif flag==0:
        next_move=random.choice(list(set1))
        flag=1
    set1=set1.difference({next_move})
    set2=set2.union({next_move})
    print('AI has made the move: {}'.format(next_move))
    return set1,set2,set3

def my_move(set1,set2,set3):
    # set1 is remaining place list, set2 is AI already placed list, set3 is my placed list
    while True:
        temp=input("What is your next move[1-9]:")
        if temp.isnumeric() and int(temp)<=9 and int(temp)>=1:
            next_move=int(temp)
            break
        else:
            print("INVALID INPUT!! Please input an integer between 1 and 9")
            continue
    set1=set1.difference({next_move})
    set3=set3.union({next_move})
    return set1,set2,set3

def choose_symbol():
    while True:
        symbol=input("PLease choose your symbol['O' or 'X']:")
        if symbol == 'O' or symbol == 'X':
            print('Okay, you will play {}'.format(symbol))
            return symbol
        else:
            print("Only 'O' or 'X' are accepted!")
            continue

def who_goes_first():
    result=random.randint(0,1)
    if result == 0:
        print('This round AI goes first.')
        return 'AI'
    else:
        print('This round YOU go first.')
        return 'me'

def play():
    my_symbol=choose_symbol()
    set1={1,2,3,4,5,6,7,8,9}
    set2=set()
    set3=set()
    player1=who_goes_first()
    if player1=='AI':
        while True:
            set1,set2,set3=AI_move(set1,set2,set3)
            if my_symbol=='O':
                print_board(set1,set3,set2)
            else:
                print_board(set1,set2,set3)
            if is_win(set2):
                print('AI wins.')
                break
            elif set1==set():
                print('Draw!')
                break
            set1,set2,set3=my_move(set1,set2,set3)
            if my_symbol=='O':
               print_board(set1,set3,set2)
            else:
               print_board(set1,set2,set3)
            if is_win(set3):
                print('You win')
                break
            elif set1==set():
                print('Draw!')
                break 
    elif player1=='me':
        while True:
            set1,set2,set3=my_move(set1,set2,set3)
            if my_symbol=='O':
               print_board(set1,set3,set2)
            else:
               print_board(set1,set2,set3)
            if is_win(set3):
                print('You win')
                break
            elif set1==set():
                print('Draw!')
                break
            set1,set2,set3=AI_move(set1,set2,set3)
            if my_symbol=='O':
               print_board(set1,set3,set2)
            else:
               print_board(set1,set2,set3)
            if is_win(set2):
                print('AI wins')
                break
            elif set1==set():
                print('Draw!')
                break



play()
# AI_move({8, 2, 4},{9, 3, 7},{1, 5, 6})


