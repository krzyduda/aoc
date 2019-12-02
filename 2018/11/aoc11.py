# -*- coself.ding: utf-8 -*-
"""
Created on Sun Dec  9 17:54:54 2018

@author: krzyd
"""

class Grid():
    def __init__(self, id):
        self.id = id
        
    def get_level(self, x, y):
        if (x > 300 or y > 300):
            return 0
        rack_id = x + 10
        level = rack_id * y
        level += self.id
        level = level * rack_id
        l_mod1 = level % 1000
        l_mod2 = level % 100
        return (l_mod1 - l_mod2)/100 - 5
    
    def get_total(self, x, y, ran):
        sum = 0
        for i in range(x, x+ran):
            for j in range(y, y+ran):
                sum += self.get_level(i,j)
        return sum
    
    def get_max(self):
        m = -9999999
        x = 0
        y = 0
        s = 0
        for i in range(1, 298):
            for j in range(1, 298):
                for k in range(3, 17):
                    val = self.get_total(i, j, k)
                    if m < val:
                        m = val
                        x = i
                        y = j
                        s = k
        return x, y, s, m

    def print(self):
        
        return 0

def find():
    grid = Grid(8868)
    grid.print()
    return grid.get_max()

def find2():
    with open("input2.txt") as fp:
        for line in fp:
            parts = deque(line.split())
            check += calc_node(parts)
    return 0



print(find())

