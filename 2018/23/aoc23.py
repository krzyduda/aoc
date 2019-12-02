# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 10:51:02 2018

@author: krzyd
"""

def calc_dist(bot1, bot2):
    return abs(bot1.x - bot2.x) + abs(bot1.y - bot2.y) + abs(bot1.z - bot2.z)

class Bot():
    def __init__(self, pos, r):
        self.r = r
        x, y, z = [int(i) for i in pos.split(',')]
        self.x = x
        self.y = y
        self.z = z
        self.count = 0

    def rang(self, bot):
        dist = calc_dist(self, bot)
        if dist <= self.r:
            self.count += 1

def find():
    bots = []
    best_range = 0
    best = 0
    idx = 0
    minx = 49425704
    miny = 49425704
    minz = 49425704
    maxx = -49425704
    maxy = -49425704
    maxz = -49425704
    with open("input.txt") as fp:
        for line in fp:
            parts = line.split()
            pos = parts[0][5:-2]
            r = int(parts[1][2:])
            if r > best_range:
                best = idx
                best_range = r
            bot = Bot(pos, r)
            bots.append(bot)
            for b in bots:
                bot.rang(b)
                b.rang(bot)
            idx += 1
        
    
    for b in bots:
        
            
    print(best)
                
    return bots[best].count - 1
    

def find2():
    with open("input2.txt") as fp:
        for line in fp:
            parts = deque(line.split())
            check += calc_node(parts)
    return 0



print(find())