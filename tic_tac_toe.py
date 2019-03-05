#!/usr/bin/env python

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

print_board({8,9,4,6,1,2},{7,3},{5})
