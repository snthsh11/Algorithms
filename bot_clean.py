# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 16:05:11 2016

@author: Santhosh
"""

import math
def dirtycells(board):
    dcell=[]
    row=col=0
    for i in board:
        col=0
        for j in i:
            if j=='d':
                dcell.append((row,col))
            col+=1
        row+=1
    print dcell
    return dcell
def distance(t1,t2):
    return math.sqrt((t1[0]-t2[0])**2+(t1[1]-t2[1])**2)
    
def next_move(posr, posc, board):
    dist=[]
    dirt_dict=dict()
    dirty_cells=dirtycells(board)
    for dcell in dirty_cells:
            dist_calc=distance(dcell,(posr,posc))
            dist.append(dist_calc)
            dirt_dict[dcell]=dist_calc
    dist.sort()
    control=len(dist)
    while control>0:
        bot_pt=(posr,posc)
        dirt_pt=dirt_dict.keys()[dirt_dict.values().index(dist[0])]
        if bot_pt==dirt_pt:
            print "CLEAN"
            del dist[0]
            control-=1
        elif bot_pt[0]==dirt_pt[0]:
            if bot_pt[1]<dirt_pt[1]:
                print "RIGHT"
                posc=bot_pt[1]+1
            elif bot_pt[1]>dirt_pt[1]:
                print "LEFT"
                posc=bot_pt[1]-1
        elif bot_pt[1]==dirt_pt[1]:
            if bot_pt[0]<dirt_pt[0]:
                print "DOWN"
                posr=bot_pt[0]+1
            elif bot_pt[0]>dirt_pt[0]:
                print "UP"
                posr=bot_pt[0]-1
        else:
            if bot_pt[0]<dirt_pt[0]:
                print "DOWN"
                posr=bot_pt[0]+1
            else:
                print "UP"
                posr=bot_pt[0]-1
        
if __name__ == "__main__":
    pos = [int(i) for i in raw_input().strip().split()]
    board = [[j for j in raw_input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
