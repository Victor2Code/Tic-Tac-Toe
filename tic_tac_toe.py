#!/usr/bin/env python

import random

def print_board(set1,set2,set3):
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
    for i in set1:
        if is_win(set2 | {i}):
            next_move=i
            break
    for i in set1:
        if is_win(set3 | {i}):
            next_move=i
            break
    if len({1,3,7,9} & set1)>0:
        next_move=random.choice(list({1,3,7,9} & set1))
    elif {5}.issubset(set1):
        next_move=5
    else:
        next_move=random.choice(list(set1))
    set1=set1.difference({next_move})
    set2=set2.union({next_move})
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
    set2=set2.union({next_move})
    return set1,set2,set3

a,b,c=my_move({1,2,3,4,6,8},{7},{5,9})
print(a)
print(b)
print(c)
