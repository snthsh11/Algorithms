# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 19:49:37 2016

@author: Santhosh
"""

#Save Princess part II
def nextMove(n,r,c,grid):
    i=j=0
    for row in grid:
        if 'p' in row:
            for col in row:
                if col=='p':
                    ro=i
                    co=j
                j+=1
        i+=1
    if ro==r and co<c:
        return "LEFT"
    elif ro==r and co>c:
        return "RIGHT"
    elif co==c and ro<r:
        return "UP"
    elif co==c and ro>r:
        return "DOWN"
    elif ro<r:
        return "UP"
    else:
        return "DOWN"
    
n = input()
r,c = [int(i) for i in raw_input().strip().split()]
grid = []
for i in xrange(0, n):
    grid.append(raw_input())

print nextMove(n,r,c,grid)
