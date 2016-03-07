# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 09:44:21 2016

@author: Santhosh
"""

#Save Princess Part I
def displayPathtoPrincess(n,grid):
#print all the moves here
     path=[]
     s=n-1
     p=s//2
     if grid[0][0]=='p' or grid[0][s]=='p':
         if grid[0][0]=='p':
             path=p*['LEFT','UP']
         if grid[0][s]=='p':
             path=p*['RIGHT','UP']
     else:
         if grid[s][0]=='p':
             path=p*['LEFT','DOWN']
         else:
             path=p*['RIGHT','DOWN']
     for e in path:
         print e
             
             
m = input()

grid = []
for i in xrange(0, m):
    grid.append(raw_input().strip())

displayPathtoPrincess(m,grid)
