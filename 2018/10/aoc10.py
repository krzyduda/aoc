# -*- coself.ding: utf-8 -*-
"""
Created on Sun Dec  9 17:54:54 2018

@author: krzyd
"""

def find():
    idx = 0
    positionx = []
    positiony = []
    velocityx = []
    velocityy = []
    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0
    
    with open("input.txt") as fp:
        for line in fp:
            parts = line.split(">")
            pos_parts = parts[0][10:].split(",")
            vel_parts = parts[1][11:].split(",")
            print(pos_parts)
            print(vel_parts)
            pos_x = int(pos_parts[0])
            pos_y = int(pos_parts[1])
            vel_x = int(vel_parts[0])
            vel_y = int(vel_parts[1])
            
            positionx.append(pos_x)
            positiony.append(pos_y)
            velocityx.append(vel_x)
            velocityy.append(vel_y)
            idx += 1
    
    lines = {}
    
    seconds = 10000
    
    for p in range(idx):
        positionx[p] = positionx[p] + seconds*velocityx[p]
        positiony[p] = positiony[p] + seconds*velocityy[p]
        
    min_x = min(positionx)
    max_x = max(positionx)
    min_y = min(positiony)
    max_y = max(positiony)
    
    print("x: ", min_x, max_x)
    print("y: ", min_y, max_y)
    
    #build
    for l in range(min_y, max_y+1):
        lines[l] = ['.' for x in range(min_x, max_x+1)]
    
    #insert
    for p in range(idx):
        x = positionx[p]
        y = positiony[p]
        
        lines[y][x-min_x] = '#'
    
    #print
    for l in range(min_y, max_y+1):
        print(''.join(lines[l]))
    
    return 0

def find2():
    with open("input2.txt") as fp:
        for line in fp:
            parts = deque(line.split())
            check += calc_node(parts)
    return 0


print(find())

