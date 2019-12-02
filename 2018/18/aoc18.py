# -*- coself.ding: utf-8 -*-
"""
Created on Sun Dec  9 17:54:54 2018

@author: krzyd
"""

tr = '|'
lm = '#'
op = '.'

class Wood():
    def __init__(self, size):
        self.size = size
        self.lines = []
        
    def add_line(self, line):
        self.lines.append(list(line)[:-1])
        
    def grow(self):
        new = []
        for x, l in enumerate(self.lines):
            new.append([])
            for y, p in enumerate(l):
                old = self.get_state(x, y)
                st = self.get_status(x, y)
                new[x].append(st)
        self.lines = new
        
    def get_state(self, x, y):
        if x < 0 or x >= self.size or y < 0 or y >= self.size:
            return op
        else:
            return self.lines[x][y]
        
    def get_status(self, x, y):
        trees = 0
        lumber = 0
        for i in range(x-1, x+2):
            for k in range(y-1, y+2):
                st = self.get_state(i, k)
                if tr is st:
                    trees += 1
                elif lm is st:
                    lumber += 1
        curr = self.get_state(x, y)
        new = str(curr)
        if tr is curr:
            trees -= 1
            if lumber >= 3:
                new = lm
        elif lm is curr:
            lumber -= 1
            if lumber == 0 or trees == 0:
                new = op
        else:
            if trees >= 3:
                new = tr
        return new
        
    def calculate(self):
        trees = 0
        lumbers = 0
        for l in self.lines:
            trees += ''.join(l).count(tr)
            lumbers += ''.join(l).count(lm)
        return trees * lumbers
    
def find():
    wood = Wood(50)
    with open("input.txt") as fp:
        for line in fp:
            wood.add_line(line)

    d = {}
        
    for i in range(1500):
        wood.grow()
        c = wood.calculate()
        d[i % 28] = c
        
    print(d)
        
    print(d[999999999 % 28])
    
    return wood.calculate()
    

def find2():
    with open("input2.txt") as fp:
        for line in fp:
            parts = deque(line.split())
            check += calc_node(parts)
    return 0



print(find())

